# LLM Project Template: OpenRouter & DSPy Integration

This project provides a boilerplate for connecting to multiple LLMs via **OpenRouter** and building structured, optimized AI pipelines using **DSPy**. It uses **uv** for extremely fast, reproducible Python environment management.

---

## 🚀 Quick Start

Follow these steps to get your environment set up and test your LLM connections.

### 1. Initialize the Project

First, ensure you have [uv](https://docs.astral.sh/uv/) installed. Then, initialize the environment:

```bash
# Create the virtual environment and lockfile
uv init -p 3.13 # <-- choose any version you like

```

### 2. Install Dependencies

Add the necessary packages for environment management, OpenAI compatibility, and DSPy:

```bash
uv add pydantic-settings openai dspy

```

### 3. Setup Environment Variables

To authenticate with OpenRouter, you must provide an API key.

1. **Grab your API key:** Visit [OpenRouter.ai](https://openrouter.ai/keys) to create a key.
2. **Create your .env file:**
* Find the `example.env` file in the root directory.
* Paste your API key into the `OPENROUTER_API_KEY` field.
* **Rename** the file from `example.env` to `.env`.



> [!IMPORTANT]
> The `.env` file is ignored by Git to keep your credentials safe. Never commit this file.

---

## 🛠️ Project Structure

The repository is focused on core logic and configuration:

* `main.py`: A script to test and compare different models defined in your config.
* `main_dspy.py`: A basic implementation of a DSPy pipeline using OpenRouter.
* `utils/llm_utils.py`: Helper functions for standard LLM completions.
* `config.py`: Centralized Pydantic settings for API keys and model identifiers.

---

## 🧪 Testing the Connections

You can use `uv` to run the scripts directly, which handles the virtual environment for you.

### Test Multiple Models

Run the standard testing script to verify that OpenRouter can reach models like Gemini, GPT-4o, and GLM:

```bash
uv run main.py

```

### Test DSPy Integration

Run the DSPy script to see how structured signatures and Chain-of-Thought reasoning work:

```bash
uv run main_dspy.py

```

---

## 🧩 How to Add New Models

To add a new model to your project, simply update the `Settings` class in `config.py`:

1. Find the model identifier on the [OpenRouter Models page](https://openrouter.ai/models).
2. Add it to the class:
```python
NEW_MODEL: str = "author/model-name"

```
