# Lesson 1: Using Previous Response ID for Context

## The Problem: Statelessness
By default, every API call is "stateless." This means the AI has no memory of what it told you in a previous request. If the AI writes a story about a character named Jax, and you then ask "What color is his suit?", the AI won't know who "he" is or that you're talking about the Jax story.

Why can't we just write a followup without a response ID? Because without it, the AI is starting from a blank slate every time, and you'd have to re-explain the whole story in every new message.

## The Solution: Response ID Referencing
We use the **Response ID** from the first interaction as a "hook." By sending a `previous_response_id` in our second request, we're telling the AI to "look back at this specific previous message" for context. This allows for a simple two-step conversation without re-sending the entire story.

## Description
This script builds on Lesson 0 but adds a follow-up step:
- **Story ID**: When the first story is generated, we capture its `id`.
- **Contextual Follow-up**: We send a second question AND that `id` so the AI remembers the story's context.

## Prerequisites
- **Python 3.7+**: [Python 3 Documentation](https://docs.python.org/3/)
- **OpenAI API Key**: [OpenAI Platform](https://platform.openai.com/)
- **SDK**: `pip install openai python-dotenv`

## Setup
1. Use the existing `.env` file in the project root with your `OPENAI_API_KEY` and `OPENAI_MODEL`.
```
OPENAI_API_KEY=your_actual_key_here
OPENAI_MODEL=gpt-5-nano
```

## How to Run
1. Navigate to this directory.
2. Run: `python story_followup.py`
3. Enter your story elements, wait for the AI's response, and then ask a follow-up question.

## Example Usage
```
Enter character name: Jax
Enter setting: Neon Tokyo
Enter problem: missing memory card
Enter ending: noir
waiting for the response...
[Story text appears]

Write a follow-up question for the story: What was on the memory card?
waiting for the response...
[AI's response based on the Jax story]
```

## Notes & Documentation
- **API Reference**: [Response Object (ID)](https://platform.openai.com/docs/api-reference/responses/object)
- **Response Creation**: [Using previous_response_id](https://platform.openai.com/docs/api-reference/responses/create)
- The script uses the model specified in your `.env` file via the `OPENAI_MODEL` variable.
- Note: This is an efficient way to link two messages without sending a full history array.
