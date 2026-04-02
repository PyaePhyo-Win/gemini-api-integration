# 🤖 Gemini API Learning Project

This project contains a series of Jupyter notebooks designed to explore the capabilities of the Google Gemini API, from basic requests to advanced features like structured outputs and automated prompt evaluation.

## 📂 Project Structure

```text
.
├── assets/                 # Images and other static files
│   └── mushroom.jpg
├── data/                   # Generated datasets and evaluation results
│   ├── eval_dataset.json
│   ├── dataset_fns.json
│   ├── results_fns.json
│   ├── dataset_complete.json
│   └── results_complete.json
├── notebooks/              # All exercise and tutorial notebooks
│   ├── accessing_gemini_api/ # Core API features
│   │   ├── make_request.ipynb
│   │   ├── chat_session.ipynb
│   │   ├── chat_exercise.ipynb
│   │   ├── system_prompt.ipynb
│   │   ├── temperature.ipynb
│   │   ├── response_streaming.ipynb
│   │   └── structured_data.ipynb
│   └── prompt_evaluation/  # Automated evaluation workflows
│       ├── prompt_evals.ipynb          # Simple dataset generation
│       ├── prompt_evals_fns.ipynb      # End-to-end evaluation pipeline
│       └── prompt_evals_complete.ipynb # Criterion-based expert evaluation
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

### 🔗 Accessing Gemini API
- **`make_request.ipynb`**: Your first steps. Learn how to initialize the client, send a prompt, and include an image.
- **`chat_session.ipynb`**: Understand how the `chats.create()` API maintains conversation state automatically.
- **`chat_exercise.ipynb`**: A practical exercise using Python's `input()` to build a real-time terminal-style chat.
- **`system_prompt.ipynb`**: Learn how to use `system_instruction` to give the model a specific persona.
- **`temperature.ipynb`**: Experiment with the `temperature` parameter to control response "creativity".
- **`response_streaming.ipynb`**: Learn how to process long responses in real-time as they are generated.
- **`structured_data.ipynb`**: Learn how to use Gemini's Controlled Generation (Structured Outputs) with Pydantic.

### 📊 Prompt Evaluation
- **`prompt_evals.ipynb`**: Generates an initial evaluation dataset of AWS-related coding tasks.
- **`prompt_evals_fns.ipynb`**: Implements a full pipeline: generates tasks, executes them, and performs dual grading (syntax validation + Gemini model review).
- **`prompt_evals_complete.ipynb`**: The most advanced version. It generates task-specific criteria (rubrics) during dataset creation and uses them to perform expert-level, criterion-based evaluations.

## 📚 Learning Resources

This project was inspired by and built alongside the following learning materials:

*   **Anthropic Skilljar Course**: [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) - Adapted and migrated to use the Google Gemini SDK for learning purposes.

## 🛡️ Security
This project uses a `.gitignore` to ensure your `.env` file and `.venv` folders are never committed to source control. Always keep your API keys private.
