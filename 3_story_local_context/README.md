# Lesson 3: Manual Context Control and Local Persistence

## The Problem: Persistence and Control
Even with a conversation ID, everything is lost once the script stops. If your internet disconnects or you close the terminal, the story is gone. We also don't have direct control over exactly what the AI "sees" in its memory.

Why do we want to manually manage history? Because it gives us total control over:
1. **Persistence**: We can save the story to a file and reload it next year!
2. **Context Trimming**: We can cut out old or irrelevant messages to stay within token limits.

## The Solution: Local History Management
We'll use a **JSON** file to store our conversation history on the computer's hard drive. Every time we send a new message, we load the history from the file, add our new message, send the whole history array to the AI, and then save the new response back to the file. This way, the "memory" is in your hands.

## Description
This is our most advanced script:
- **Local JSON Storage**: Saves the entire history to a `.agent` file.
- **System Role**: We add a special "system" prompt to tell the AI it's a short story writer.
- **Context Trimming**: We keep only the last 10 messages (`CONTEXT_LIMIT`) to maintain a clean and relevant conversation.

## Prerequisites
- **Python 3.7+**: [Python 3 JSON Documentation](https://docs.python.org/3/library/json.html)
- **OpenAI API Key**: [OpenAI Platform](https://platform.openai.com/)
- **SDK**: `pip install openai python-dotenv`

## Setup
1. Use the existing `.env` file in the project root with your `OPENAI_API_KEY`.

## How to Run
1. Navigate to this directory.
2. Run: `python story_local_context.py`
3. Generate your story and continue it with follow-ups.
4. Close the script and restart it to see how the AI "remembers" everything from before!

## Example Usage
```
Enter character name: Silas
Enter setting: Neon City
Enter problem: missing memory chip
Enter ending: noir
waiting for the response...
API response: [Story text]

What's next? Silas enters a rainy alleyway.
waiting for the response...
API response: [Story continues]
```

## Notes & Documentation
- **API Reference**: [Input (History Array)](https://platform.openai.com/docs/api-reference/responses/create)
- **OpenAI Developer Guide**: [Managing Context](https://platform.openai.com/docs/guides/text-generation)
- Note: This is a powerful pattern for building persistent AI assistants.
