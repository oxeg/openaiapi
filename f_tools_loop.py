import json
import os
from pathlib import Path

import openai
from dotenv import load_dotenv
from openai import OpenAI


def read_file(filename):
    print(f"--> [TOOL executing] Reading file: {filename}")

    if not Path(filename).exists():
        return json.dumps({"content": "", "error": "file not found"})

    with open(filename, 'r') as file:
        content = file.read()

    print(f"--> [TOOL response] File read: {len(content)} bytes")
    return json.dumps({"content": content, "error": None})


def write_file(filename, content=""):
    print(f"--> [TOOL executing] Writing file {filename} with content: {len(content)} bytes")

    full_path = ''
    with open(filename, 'w') as file:
        file.write(content)
        full_path = Path(filename).resolve()

    print(f"--> [TOOL executing] File {full_path} written.")
    return json.dumps({"status": "success"})


tools = [
    {
        "type": "function",
        "name": "read_file",
        "description": "Read the contents of a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The name of the file to read."
                }
            },
            "required": ["filename"]
        }
    },
    {
        "type": "function",
        "name": "write_file",
        "description": "Write content to a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The name of the file to write to."
                },
                "content": {
                    "type": "string",
                    "description": "Content of the file to write."
                }
            },
            "required": ["filename", "content"]
        }
    }
]

available_functions = {
    "read_file": read_file,
    "write_file": write_file
}

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
conversation = openai.conversations.create()

while True:
    try:
        prompt = input("Write a task: ")

        if prompt.lower() in ['quit', 'exit']:
            break

        print("waiting for the response...")

        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
            tools=tools,
            tool_choice="auto",
            conversation=conversation.id,
        )

        print(response.output_text)

        for item in response.output:
            if hasattr(item, 'type') and item.type == 'function_call':
                print(f"AI run calls a tool: {item.name}")

                fn_name = item.name
                fn_args = json.loads(item.arguments)

                if fn_name in available_functions:
                    fn_result = available_functions[fn_name](**fn_args)
                else:
                    fn_result = json.dumps({"error": "Unknown function"})

                fn_result = json.dumps({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(fn_result)
                })

                response = client.responses.create(
                    model="gpt-5-nano",
                    input=fn_result,
                    conversation=conversation.id,
                )

                print(response.output_text)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
