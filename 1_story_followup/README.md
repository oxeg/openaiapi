# Story Followup

An extension of the story generator that allows users to ask a single follow-up question about the generated story.

## Description

This script prompts the user for four key story elements and then generates a story. After the story is created, it allows for a follow-up interaction:
- **Story Generation**: Uses character, setting, problem, and ending to create an initial tale.
- **Follow-up Question**: Prompts the user for a question about the story.
- **Contextual Answer**: Uses OpenAI's `previous_response_id` to provide an answer that maintains context with the generated story.

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
python story_followup.py
```

3. Follow the prompts to enter your story elements:
   - Character name
   - Setting
   - Problem
   - Ending type
4. Once the story is generated, enter a follow-up question.
5. Wait for the AI to answer based on the story's context.

## Example Usage

```
Enter character name: Jax the Robot
Enter setting: a scrap yard
Enter problem: running out of battery
Enter ending: triumphant
waiting for the response...
[Initial story appears here]

Write a follow-up question for the story: Does Jax find a new power source?
waiting for the response...
[AI's contextual answer appears here]
```


## Notes

- The script uses OpenAI's `gpt-5-nano` model for story generation
- Make sure your `.env` file is never committed to version control (add it to `.gitignore`)
- API usage may incur costs depending on your OpenAI plan
