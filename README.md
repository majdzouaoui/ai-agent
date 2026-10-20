# AI Coding Agent

A Python AI coding agent built with the OpenAI SDK and OpenRouter as part of the Boot.dev Learn to Code in Python curriculum.

The agent uses an LLM with function calling to inspect files, read and write code, execute Python scripts, and iteratively solve coding tasks.

## Features

- **File inspection:** List files and directories, including file sizes and directory information.
- **File reading:** Read file contents with safeguards against accessing files outside the working directory.
- **File writing:** Create or update files within the permitted working directory.
- **Python execution:** Run Python scripts and return their output.
- **Tool calling:** Let the LLM select and execute tools based on the user's request.
- **Agent loop:** Process tool calls iteratively until the agent produces a final response or reaches the iteration limit.
- **Verbose mode:** Display tool calls and token usage for debugging and monitoring.

## Technologies Used

- Python
- OpenAI Python SDK
- OpenRouter API
- `uv` for Python project and dependency management
- Git and GitHub

## Project Structure

```text
aiagent/
├── main.py
├── prompts.py
├── call_function.py
├── config.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/
│   ├── main.py
│   ├── tests.py
│   ├── README.md
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-agent.git
cd ai-agent
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Security:** Never commit or share your `.env` file or API key.

### 4. Run the agent

Ask the agent to perform a task:

```bash
uv run main.py "How does the calculator render results to the console?"
```

Enable verbose mode to inspect tool calls and token usage:

```bash
uv run main.py "Explain the calculator project" --verbose
```

## Example Tasks

The agent can handle requests such as:

- "List the files in the project."
- "Explain how the calculator renders results."
- "Fix the bug in the calculator."
- "Create a Python file that calculates the average of a list."
- "Run the calculator tests."

The results depend on the model's capabilities and the tools available to the agent.

## What I Learned

- Integrating an LLM through an API
- Implementing function calling and tool execution
- Designing tools with structured arguments
- Building an iterative agent loop
- Reading, writing, and executing files safely
- Managing Python dependencies with `uv`
- Debugging and testing an AI-powered application

## Future Improvements

- Add more tools and automated tests
- Improve error handling and input validation
- Add conversation history and more robust execution limits
- Explore different models and compare their performance

## Acknowledgements

Built as part of the [Boot.dev](https://www.boot.dev/) Python learning curriculum.

## License

This project is intended for educational purposes.&#x20;
