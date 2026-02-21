import json
import os
from time import sleep

from dotenv import load_dotenv
from openai import OpenAI

STORAGE_FILE = ".agent"
CONTEXT_LIMIT = 10


def load_history():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    else:
        return [{"role": "system", "content": "You are a short story writer. Write a short story based on provided input, no longer than 20 sentences."}]


def save_history(history):
    temp_file = STORAGE_FILE + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(history, f, indent=4)
    os.replace(temp_file, STORAGE_FILE)


def trim_history(history):
    if len(history) > CONTEXT_LIMIT:
        return history[-CONTEXT_LIMIT:]
    return history


def main():
    load_dotenv()
    history = load_history()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    client = OpenAI(api_key=api_key)

    character = input("Enter character name: ")
    setting = input("Enter setting: ")
    problem = input("Enter problem: ")
    ending = input("Enter ending: ")

    prompt = f"Write a fun short story about a character {character} in a {setting} setting who faces the problem {problem}. The ending should be {ending}."
    history.append({"role": "user", "content": prompt})

    print("waiting for the response...")

    response = client.responses.create(
        model=model,
        input=history
    )

    ai_response = response.output_text
    print(f"API response: {ai_response}")

    history.append({"role": "assistant", "content": ai_response})
    save_history(history)

    while True:
        try:
            sleep(2)

            prompt = input("What's next? ")

            if prompt.lower() in ['quit', 'exit']:
                break

            print("waiting for the response...")

            history.append({"role": "user", "content": prompt})
            history = trim_history(history)

            response = client.responses.create(
                model=model,
                input=history
            )

            ai_response = response.output_text
            print(f"API response: {ai_response}")

            history.append({"role": "assistant", "content": ai_response})
            history = trim_history(history)
            save_history(history)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
