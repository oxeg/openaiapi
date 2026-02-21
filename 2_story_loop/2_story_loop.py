import os
from time import sleep

import openai
from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)
    conversation = openai.conversations.create()

    character = input("Enter character name: ")
    setting = input("Enter setting: ")
    problem = input("Enter problem: ")
    ending = input("Enter ending: ")

    prompt = f"Write a fun short story about a character {character} in a {setting} setting who faces the problem {problem}. The ending should be {ending}."

    print("waiting for the response...")

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt,
        conversation=conversation.id
    )

    print(response.output_text)

    while True:
        try:
            sleep(2)

            prompt = input("What's next? ")

            if prompt.lower() in ['quit', 'exit']:
                break

            print("waiting for the response...")

            response = client.responses.create(
                model="gpt-5-nano",
                input=prompt,
                conversation=conversation.id
            )

            print(response.output_text)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
