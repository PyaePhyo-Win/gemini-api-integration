# 🤖 Gemini API Learning Project

This project contains a series of Jupyter notebooks designed to explore the capabilities of the Google Gemini API, from basic requests to advanced features like system prompts and temperature control.

## 📂 Project Structure

```text
.
├── assets/                 # Images and other static files
│   └── mushroom.jpg
├── notebooks/              # All exercise and tutorial notebooks
│   ├── chat-exercise.ipynb # Interactive chat loop with input()
│   ├── chat-session.ipynb  # Multi-turn conversation logic
│   ├── make-request.ipynb  # Basic API calls and image processing
│   ├── system-prompt.ipynb # Behavioral control using System Instructions
│   └── temperature.ipynb   # Deterministic vs. Creative model tuning
├── .env                    # (Local only) API keys and secrets
├── .gitignore              # Files excluded from version control
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

1.  **Environment Setup**:
    Ensure you have Python installed and create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **API Key Configuration**:
    Create a `.env` file in the root directory and add your Google AI Studio API key:
    ```text
    GOOGLE_API_KEY=your_api_key_here
    ```

## 📓 Notebook Descriptions

- **`make-request.ipynb`**: Your first steps. Learn how to initialize the client, send a prompt, and include an image in your request.
- **`chat-session.ipynb`**: Understand how the `chats.create()` API maintains conversation state automatically.
- **`chat-exercise.ipynb`**: A practical exercise using Python's `input()` to build a real-time terminal-style chat inside a notebook.
- **`system-prompt.ipynb`**: Learn how to use `system_instruction` to give the model a specific persona (like a Math Tutor).
- **`temperature.ipynb`**: Experiment with the `temperature` parameter to control the "creativity" or "predictability" of responses.

## 📚 Learning Resources

This project was inspired by and built alongside the following learning materials:

*   **Anthropic Skilljar Course**: [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) - An excellent resource for understanding the fundamentals of working with large language model APIs.

## 🛡️ Security
This project uses a `.gitignore` to ensure your `.env` file and `.venv` folders are never committed to source control. Always keep your API keys private.
