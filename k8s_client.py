import asyncio
import json
import os

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import AsyncOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
ai_model = os.getenv("OPENAI_MODEL")

openai_client = AsyncOpenAI(api_key=api_key)

# Adjust this to point to your server (Python or Go)
# IF GO SERVER:
# server_params = StdioServerParameters(
#     command="./k8s-mcp-server",
#     args=[],
#     env=os.environ
# )

server_params = StdioServerParameters(
    command="python",
    args=["k8s_server.py"],
    env=os.environ
)

async def get_user_input(prompt: str) -> str:
    """
    Non-blocking input function.
    Runs input() in a separate thread so it doesn't block the asyncio event loop.
    """
    return await asyncio.to_thread(input, prompt)


async def run_chat_loop():
    print("--- Starting Interactive Kubernetes Assistant (MCP) ---")
    print("Connecting to local MCP server...")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_response = await session.list_tools()
            openai_tools = [{
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema
                }
            } for tool in tools_response.tools]

            print(f"Connected! Loaded {len(openai_tools)} tools.")
            print("Type 'quit', 'exit', or 'q' to stop.\n")

            messages = [
                {"role": "system",
                 "content": "You are a helpful Kubernetes Assistant. You have access to tools to manage the cluster. Always ask for confirmation before deleting resources."}
            ]

            while True:
                try:
                    user_text = await get_user_input("\nUser: ")

                    if user_text.lower() in ["quit", "exit", "q"]:
                        print("Goodbye!")
                        break

                    if not user_text.strip():
                        continue

                    messages.append({"role": "user", "content": user_text})

                    response = await openai_client.chat.completions.create(
                        model=ai_model,
                        messages=messages,
                        tools=openai_tools
                    )

                    # --- Tool Loop ---
                    # We loop because the model might want to call multiple tools in sequence
                    # or the tool output might prompt further tool calls.
                    while response.choices[0].message.tool_calls:

                        assistant_msg = response.choices[0].message
                        messages.append(assistant_msg)  # Add the "I want to call a tool" message to history

                        tool_calls = assistant_msg.tool_calls

                        for tool_call in tool_calls:
                            fn_name = tool_call.function.name
                            fn_args = json.loads(tool_call.function.arguments)

                            print(f"AI: [Tool Call] {fn_name}({fn_args})")

                            try:
                                result = await session.call_tool(fn_name, arguments=fn_args)
                                tool_output = result.content[0].text  # Extract text content
                            except Exception as e:
                                tool_output = f"Error executing tool: {str(e)}"

                            messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": tool_output
                            })
                            print(f"AI: [Tool Result] {tool_output}")

                        response = await openai_client.chat.completions.create(
                            model=ai_model,
                            messages=messages,
                            tools=openai_tools
                        )

                    final_text = response.choices[0].message.content
                    print(f"AI: {final_text}")

                    messages.append({"role": "assistant", "content": final_text})

                except Exception as e:
                    print(f"An error occurred in the loop: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(run_chat_loop())
    except KeyboardInterrupt:
        print("\nExiting...")