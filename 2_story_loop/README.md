# Story Loop

A conversational story assistant that allows for continuous interaction and story development through a persistent conversation loop.

## Description

This script introduces a conversation loop, allowing for an ongoing narrative. It manages the session using OpenAI's conversation management:
- **Initial Story**: Generates a story based on the character, setting, problem, and ending provided by the user.
- **Interactive Loop**: After the initial story, the user can continue the narrative by providing further input ("What's next?").
- **Persistent Context**: Uses a `conversation.id` to ensure the AI remembers the entire thread of the discussion.

## Prerequisites

Before running this script, ensure you have:

1. **Python 3.7+** installed on your system
2. **OpenAI API Key**: You'll need an active OpenAI API key. You can get one from [OpenAI's platform](https://platform.openai.com/)
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

1. Navigate to the project directory in your terminal
2. Run the script:
```shell script
python story_loop.py
```

3. Follow the prompts to enter your story elements:
   - Character name
   - Setting
   - Problem
   - Ending type
4. Use the "What's next?" prompt to continue the story or ask about details.
5. Type `quit` or `exit` to end the session.

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

- The script uses OpenAI's `gpt-5-nano` model for story generation
- Make sure your `.env` file is never committed to version control (add it to `.gitignore`)
- API usage may incur costs depending on your OpenAI plan
