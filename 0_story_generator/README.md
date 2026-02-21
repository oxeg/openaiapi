# Lesson 0: Programmatic Text Generation

## The Problem
Manually typing prompts into a web interface is great for humans, but what if you want to build an application that generates content automatically based on user input? We need a way to capture specific variables (like a character name or a setting) and "inject" them into a prompt template that the AI can understand.

## The Solution
We use the OpenAI Python SDK to bridge the gap between user input and the AI model. By using f-strings in Python, we can programmatically construct a prompt and send it to the API, receiving a structured response that our application can then display.

## Description
This script demonstrates the basic "Request-Response" cycle:
- **Input Collection**: Uses Python's `input()` to gather story elements.
- **Prompt Engineering**: Combines those elements into a coherent instruction.
- **API Call**: Uses `client.responses.create` to send the prompt to the `gpt-5-nano` model.

## Prerequisites
- **Python 3.7+**: [Python Official Documentation](https://docs.python.org/3/)
- **OpenAI API Key**: [OpenAI API Keys](https://platform.openai.com/api-keys)
- **SDK**: Install via `pip install openai python-dotenv`

## Setup
1. Create a `.env` file in the project root.
2. Add your key: `OPENAI_API_KEY=your_actual_key_here`

## How to Run
1. Navigate to this directory.
2. Run: `python story_generator.py`

## Example Usage
```
Enter character name: Orbit the Robot
Enter setting: Mars colony
Enter problem: out of oxygen
Enter ending: heroic
waiting for the response...
[AI generates the story based on your variables]
```

## Notes & Documentation
- **Model Documentation**: [OpenAI Models Guide](https://platform.openai.com/docs/models)
- **API Reference**: [Create Response](https://platform.openai.com/docs/api-reference/responses/create)
- Always ensure your `.env` is in your `.gitignore` to prevent leaking secrets.
