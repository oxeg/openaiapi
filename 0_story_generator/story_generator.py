import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    character = input("Enter character name: ")
    setting = input("Enter setting: ")
    problem = input("Enter problem: ")
    ending = input("Enter ending: ")

    prompt = f"Write a fun short story about a character {character} in a {setting} setting who faces the problem {problem}. The ending should be {ending}."

    print("waiting for the response...")

    response = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
