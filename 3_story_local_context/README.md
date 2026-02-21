# Story Local Context

An advanced story generator that maintains conversation history locally, allowing for persistent context across script restarts.

## Description

This script manages the conversation context manually by saving the history to a local JSON file, ensuring the AI behaves as a consistent story writer:
- **Local Persistence**: Saves the entire conversation history to a `.agent` file.
- **Context Management**: Trims the history to the last 10 messages (`CONTEXT_LIMIT`) to maintain relevance and stay within limits.
- **System Role**: Uses a "system" prompt to define the AI's persona as a short story writer.
- **Interaction**: Features an ongoing loop where users can continue the story through "What's next?" prompts.

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
python story_local_context.py
```

3. Follow the prompts to enter your story elements:
   - Character name
   - Setting
   - Problem
   - Ending type
4. Use the "What's next?" prompt to continue the narrative.
5. Type `quit` or `exit` to end the session.

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

- The script uses OpenAI's `gpt-5-nano` model for story generation
- Make sure your `.env` file is never committed to version control (add it to `.gitignore`)
- API usage may incur costs depending on your OpenAI plan
