# Story Loop

A conversational story assistant that allows for continuous interaction and story development through a persistent conversation loop.

## Description

This script introduces a conversation loop, allowing the user to keep the story going indefinitely. It uses OpenAI's conversation management to track the state of the interaction.
- **Initial Prompt**: Collects character, setting, problem, and ending to start the story.
- **Interactive Loop**: After the initial story, the user can continue to ask questions or provide new directions ("What's next?").
- **Conversation State**: Uses a `conversation.id` to ensure the AI remembers the entire thread of the discussion.

## Prerequisites

Before running this script, ensure you have:

1. **Python 3.7+** installed on your system
2. **OpenAI API Key**: You'll need an active OpenAI API key.
3. **Required Python packages**: Install dependencies using pip:
```shell script
pip install openai python-dotenv
```

## Setup

1. Create a `.env` file in the project root directory
2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

## How to Run

1. Navigate to the `2_story_loop` directory in your terminal
2. Run the script:
```shell script
python story_loop.py
```

3. Enter the initial story elements to generate the first part of the tale.
4. Use the "What's next?" prompt to continue the story, ask about details, or change the direction of the narrative.
5. To exit the loop, type `quit` or `exit`.

## Example Usage

```
Enter character name: Elara
Enter setting: floating islands
Enter problem: gravity is failing
Enter ending: mysterious
waiting for the response...
[Initial story appears]

What's next? Elara finds a hidden engine room.
waiting for the response...
[Story continues with the new detail]

What's next? quit
```

## Notes

- This script creates a new conversation using `client.conversations.create()`.
- The interaction continues until the user explicitly quits.
- It uses the `gpt-5-nano` model.
