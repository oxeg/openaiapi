# Story Generator

A simple Python script that uses OpenAI's API to generate creative short stories based on user-provided story elements.

## Description

This script prompts the user to input four key story elements:
- **Character name**: The protagonist of your story
- **Setting**: Where the story takes place
- **Problem**: The challenge or conflict the character faces
- **Ending**: How the story concludes (e.g., "happy", "surprising", "tragic")

The script then sends these elements to OpenAI's API, which generates a fun, creative short story incorporating all the provided details.

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
python story_generator.py
```

3. Follow the prompts to enter your story elements:
   - Character name
   - Setting
   - Problem
   - Ending type
4. Wait for the AI to generate your story
5. Enjoy your custom-generated short story!

## Example Usage

```
Enter character name: Luna the Cat
Enter setting: enchanted forest
Enter problem: lost magical bell
Enter ending: heartwarming
waiting for the response...
[Generated story will appear here]
```


## Notes

- The script uses OpenAI's `gpt-5-nano` model for story generation
- Make sure your `.env` file is never committed to version control (add it to `.gitignore`)
- API usage may incur costs depending on your OpenAI plan