# Story Local Context

An advanced story generator that maintains conversation history locally, allowing for persistent context across script restarts.

## Description

This script manages the conversation context manually by saving the history to a local JSON file. It features:
- **Local Storage**: Saves the conversation history to a file named `.agent`.
- **Context Management**: Automatically trims the history to the last 10 messages (`CONTEXT_LIMIT`) to stay within token limits and maintain relevance.
- **System Prompt**: Uses a predefined system role to guide the AI's behavior as a short story writer.
- **Persistence**: If you restart the script, it can load the previous state from the `.agent` file.

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

1. Navigate to the `3_story_local_context` directory in your terminal
2. Run the script:
```shell script
python story_local_context.py
```

3. Enter the initial story elements.
4. Continue the interaction using the "What's next?" prompt.
5. Type `quit` or `exit` to stop.
6. Observe that a `.agent` file is created/updated in the directory, storing your conversation history.

## Example Usage

```
Enter character name: Silas
Enter setting: neon city
Enter problem: missing memory chip
Enter ending: noir
waiting for the response...
API response: [Story text]

What's next? Silas enters a rainy alleyway.
waiting for the response...
API response: [Story continues]
```

## Notes

- The conversation history is stored in `.agent` as a JSON list of message objects.
- A `.agent.tmp` file is used during saving to ensure data integrity.
- The `trim_history` function ensures the context sent to the API doesn't grow indefinitely.
- Uses the `gpt-5-nano` model.
