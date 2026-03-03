import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

STORAGE_FILE = ".agent"
CONTEXT_LIMIT = 10


def load_history():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    else:
        return [{"role": "system",
                 "content": "You are a coding assistant. Use provided tools to complete the tasks according to user input."}]


def save_history(history):
    temp_file = STORAGE_FILE + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(history, f, indent=4)
    os.replace(temp_file, STORAGE_FILE)


def trim_history(history):
    if len(history) > CONTEXT_LIMIT:
        return history[-CONTEXT_LIMIT:]
    return history


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

    print(f"--> [TOOL response] File {full_path} written.")
    return json.dumps({"status": "success"})


def main():
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
    history = load_history()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    client = OpenAI(api_key=api_key)

    while True:
        try:
            prompt = input("Write a task: ")

            if prompt.lower() in ['quit', 'exit']:
                break

            history.append({"role": "user", "content": prompt})

            print("waiting for the response...")
            response = client.responses.create(
                model=model,
                input=history,
                tools=tools,
                tool_choice="auto"
            )

            ai_response = response.output_text
            print(f"AI response: {ai_response}")

            for item in response.output:
                item_dict = item.model_dump()
                item_dict.pop("status", None)
                history.append(item_dict)

                if hasattr(item, 'type') and item.type == 'function_call':
                    print(f"AI run calls a tool: {item.name}")

                    fn_name = item.name
                    fn_args = json.loads(item.arguments)

                    if fn_name in available_functions:
                        fn_result = available_functions[fn_name](**fn_args)
                    else:
                        fn_result = json.dumps({"error": "Unknown function"})

                    fn_result = {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(fn_result)
                    }
                    history.append(fn_result)

                    response = client.responses.create(
                        model=model,
                        input=history,
                        tools=tools,
                        tool_choice="auto"
                    )

                    print(response.output_text)
                    for sub_item in response.output:
                        sub_dict = sub_item.model_dump()
                        sub_dict.pop("status", None)
                        history.append(sub_dict)

            history = trim_history(history)
            save_history(history)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
