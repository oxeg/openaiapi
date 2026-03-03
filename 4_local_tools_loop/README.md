# Lesson 4: Function Calling and Tool Use

## The Problem: Limitations of Text-Only AI
Until now, our AI could only talk. It could generate stories and remember past conversations, but it couldn't *do* anything in the real world. If you asked it to create a file or read a document on your computer, it would just simulate the action in text without actually performing it.

## The Solution: Function Calling (Tools)
Function calling allows the AI to interact with external tools and your local system. We define "tools" (Python functions) and describe them to the AI. When the AI decides it needs to perform an action, it outputs a request to call a specific function with certain arguments. Our script then executes that function and sends the result back to the AI.

## Description
This script implements a coding assistant with the following capabilities:
- **Local Tool Execution**: The AI can actually `read_file` and `write_file` on your hard drive.
- **Autonomous Loop**: If a tool is called, the script automatically sends the tool's output back to the AI so it can finish its task.
- **Persistent History**: Like in Lesson 3, it saves the conversation to a `.agent` file.
- **System Role**: Configured as a "coding assistant" to prioritize technical tasks.

## Prerequisites
- **Python 3.7+**
- **OpenAI API Key**
- **SDK**: `pip install openai python-dotenv`

## Setup
1. Use the existing `.env` file in the project root with your `OPENAI_API_KEY` and `OPENAI_MODEL`.
```
OPENAI_API_KEY=your_actual_key_here
OPENAI_MODEL=gpt-4o  # Ensure the model supports tool use
```

## How to Run
1. Navigate to this directory.
2. Run: `python local_tools_loop.py`
3. Give the assistant a task involving files, for example: "Create a file named hello.txt with the content 'Hello from the AI!'"
4. Check your folder to see the new file!

## Example Usage
```
Write a task: Create a file called notes.txt and write 'Buy milk' in it.
waiting for the response...
--> [TOOL executing] Writing file notes.txt with content: 8 bytes
--> [TOOL response] File /Users/.../notes.txt written.
AI response: I've created the file notes.txt with the content "Buy milk".
```

## Notes & Documentation
- **Function Calling**: [OpenAI Guide: Function Calling](https://platform.openai.com/docs/guides/function-calling)
- The AI does not execute the code itself; it sends a JSON object describing which function to call. Your local Python script is responsible for the actual execution, ensuring security and control.
- This pattern is the foundation for building "Agents" that can browse the web, use databases, or control hardware.
