import os
from time import sleep

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

    story = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )

    print(story.output_text)

    sleep(2)

    followup = input("Write a follow-up question for the story: ")
    print("waiting for the response...")

    answer = client.responses.create(
        model="gpt-5-nano",
        input=followup,
        previous_response_id=story.id
    )

    print(answer.output_text)


if __name__ == "__main__":
    main()
