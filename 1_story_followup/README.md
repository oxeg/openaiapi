# Story Followup

An extension of the story generator that allows users to ask a single follow-up question about the generated story.

## Description

This script builds upon the basic story generator by utilizing OpenAI's response referencing system. It first generates a story based on:
- **Character name**
- **Setting**
- **Problem**
- **Ending**

After the story is generated, it prompts the user for a **follow-up question**. The script sends this question along with the ID of the previous story response, allowing the AI to maintain context for its answer.

## Prerequisites

Before running this script, ensure you have:

1. **Python 3.7+** installed on your system
2. **OpenAI API Key**: You'll need an active OpenAI API key.
3. **Required Python packages**: Install dependencies using pip:
```shell script
pip install openai python-dotenv
```

## Setup

1. Create a `.env` file in the project root directory (if not already present)
2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

## How to Run

1. Navigate to the `1_story_followup` directory in your terminal
2. Run the script:
```shell script
python story_followup.py
```

3. Enter the initial story elements when prompted.
4. Once the story is generated, enter a follow-up question (e.g., "What happened to the side character?" or "Explain the ending more.").
5. Wait for the AI to provide an answer based on the story's context.

## Example Usage

```
Enter character name: Jax the Robot
Enter setting: a scrap yard
Enter problem: running out of battery
Enter ending: triumphant
waiting for the response...
[Story about Jax appears here]

Write a follow-up question for the story: Does Jax find a new power source?
waiting for the response...
[AI's answer based on the story appears here]
```

## Notes

- The script uses `previous_response_id` to link the follow-up question to the original story.
- It uses the `gpt-5-nano` model.
- API usage may incur costs depending on your OpenAI plan.
