# OpenAI API Storytelling Lessons

This project is a structured series of Python coding lessons designed to teach the fundamentals of the OpenAI API. Through the lens of building an AI-powered storyteller, you will learn how to manage context, handle statelessness, and build persistent AI assistants.

## Project Structure

The lessons are organized progressively, with each step solving a specific technical challenge in AI development:

- **[0_story_generator](./0_story_generator/)**: **Programmatic Text Generation**. Learn the basics of sending structured prompts to an LLM using Python and f-strings.
- **[1_story_followup](./1_story_followup/)**: **Contextual Referencing**. Understand the "stateless" nature of APIs and how to use `previous_response_id` to link two messages together.
- **[2_story_loop](./2_story_loop/)**: **Conversation Management**. Learn how to use `conversation_id` to create a stateful, interactive chat loop without manual message tracking.
- **[3_story_local_context](./3_story_local_context/)**: **Persistence & Manual Control**. Build a professional-grade assistant that saves its history to a local JSON file and manages its own context window.

## Prerequisites

- **Python 3.7+**
- **OpenAI API Key**: [Get one here](https://platform.openai.com/api-keys)

## Quick Start

1. **Install Dependencies**:
   ```shell script
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Create a `.env` file in this root directory:
   ```env
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-5-nano
   ```

3. **Run a Lesson**:
   Navigate into any lesson directory and run the corresponding Python script:
   ```shell script
   cd 0_story_generator
   python story_generator.py
   ```

## Learning Goals

- Understand the Request-Response cycle of LLMs.
- Master different methods of context management (Response IDs vs. Conversation IDs).
- Learn how to implement local storage for persistent AI memory.
- Explore basic prompt engineering and system-role definitions.
