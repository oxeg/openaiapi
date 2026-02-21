import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
ai_model = os.getenv("OPENAI_MODEL")
openai_client = OpenAI(api_key=api_key)


def k8s_list_pods(namespace="default"):
    print(f"--> [TOOL executing] Listing pods in namespace: {namespace}")
    pod_names = ['checkout-api-4a5b7c38', 'vmeconnector-e78c976a']
    print(f"--> [TOOL response] {pod_names}")
    return json.dumps({"pods": pod_names, "count": len(pod_names)})


def k8s_delete_pod(pod_name, namespace="default"):
    print(f"--> [TOOL executing] Deleting pod: {pod_name} in namespace: {namespace}")
    print(f"--> [TOOL executing] Pod: {pod_name} in namespace: {namespace}")
    return json.dumps({"status": "success", "message": f"Pod {pod_name} deleted."})


tools = [
    {
        "type": "function",
        "name": "list_pods",
        "description": "Get a list of all pods in a specific Kubernetes namespace.",
        "parameters": {
            "type": "object",
            "properties": {
                "namespace": {
                    "type": "string",
                    "description": "The namespace to list pods from (e.g., 'default', 'kube-system'). Defaults to 'default'."
                }
            },
            "required": []
        }
    },
    {
        "type": "function",
        "name": "delete_pod",
        "description": "Delete a specific pod by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "pod_name": {
                    "type": "string",
                    "description": "The name of the pod to delete."
                },
                "namespace": {
                    "type": "string",
                    "description": "The namespace where the pod is located."
                }
            },
            "required": ["pod_name"]
        }
    }
]

available_functions = {
    "list_pods": k8s_list_pods,
    "delete_pod": k8s_delete_pod
}


def chat_with_cluster():
    print("--- Kubernetes AI Assistant (Responses API) ---")
    print("Try: 'List pods in default' or 'Restart nginx deployment'")

    system_instructions = "You are a Kubernetes SRE assistant. Use the provided tools to manage the cluster."

    conversation_history = []

    while True:
        try:
            user_input = input("\nEnter command (or 'quit'): ")
            if user_input.lower() in ['quit', 'exit']:
                break

            conversation_history.append({"role": "user", "content": user_input})

            response = openai_client.responses.create(
                model=ai_model,
                instructions=system_instructions,
                input=conversation_history,
                tools=tools
            )

            tool_calls_made = False

            for item in response.output:
                if hasattr(item, 'type') and item.type == 'function_call':
                    tool_calls_made = True
                    print(f"AI run tool: {item.name}")

                    conversation_history.append(item)

                    fn_name = item.name
                    fn_args = json.loads(item.arguments)

                    if fn_name in available_functions:
                        fn_result = available_functions[fn_name](**fn_args)
                    else:
                        fn_result = json.dumps({"error": "Unknown function"})

                    conversation_history.append({
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": fn_result
                    })

                elif hasattr(item, 'content'):
                    # print(f"AI debug: {item}")
                    conversation_history.append(item)
                    if item.content and len(item.content) > 0:
                        for content in item.content:
                            if hasattr(content, 'text'):
                                print(f"AI response: {content.text}")

            if tool_calls_made:
                follow_up = openai_client.responses.create(
                    model=ai_model,
                    instructions=system_instructions,
                    input=conversation_history,
                    tools=tools
                )

                if follow_up.output_text:
                    print(f"AI follow-up: {follow_up.output_text}")
                    conversation_history.append({"role": "assistant", "content": follow_up.output_text})

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    chat_with_cluster()
