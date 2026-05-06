# Gemini API Learning Project

This repository contains a set of Jupyter notebooks for learning the Google Gemini API, multimodal inputs, grounded PDF analysis, structured outputs, prompt evaluation workflows, prompt engineering patterns, tool use, and retrieval-augmented generation (RAG) search techniques.

The project is organized around six themes:

- Accessing the Gemini API with the Google GenAI SDK
- Exploring Gemini features such as image analysis, PDF analysis, citations, and extended thinking
- Using built-in and custom tools with Gemini
- Building prompt evaluation pipelines that generate and grade datasets
- Improving prompt quality with more explicit structure and evaluation loops
- Building RAG search components with chunking, embeddings, vector search, BM25, and hybrid retrieval

## Project Layout

```text
.
├── assets/
├── data/
│   ├── chunking.md
│   ├── dataset_complete.json
│   ├── dataset_fns.json
│   ├── dataset_gemini.json
│   ├── dataset_improved.json
│   ├── eval_dataset.json
│   ├── results_complete.json
│   └── results_fns.json
├── notebooks/
│   ├── accessing_gemini_api/
│   │   ├── chat_exercise.ipynb
│   │   ├── chat_session.ipynb
│   │   ├── make_request.ipynb
│   │   ├── response_streaming.ipynb
│   │   ├── structured_data.ipynb
│   │   ├── system_prompt.ipynb
│   │   └── temperature.ipynb
│   ├── features_of_gemini/
│   │   ├── citations.ipynb
│   │   ├── extended_thinking.ipynb
│   │   ├── images.ipynb
│   │   └── pdfs.ipynb
│   ├── prompt_engineering/
│   │   ├── prompting.ipynb
│   │   └── prompting_improved.ipynb
│   ├── prompt_evaluation/
│   │   ├── prompt_evals.ipynb
│   │   ├── prompt_evals_complete.ipynb
│   │   └── prompt_evals_fns.ipynb
│   ├── rag_and_agentic_search/
│   │   ├── bm25.ipynb
│   │   ├── chunking.ipynb
│   │   ├── embeddings.ipynb
│   │   ├── hybrid.ipynb
│   │   └── vectordb.ipynb
│   └── tool_use_with_gemini/
│       ├── text_editor_tool.ipynb
│       ├── tool_functions.ipynb
│       ├── tool_streaming.ipynb
│       └── web_search_tool.ipynb
├── playground/
├── reports/
│   ├── improved_report.html
│   └── prompt_eval_report.html
├── utils/
│   ├── __init__.py
│   └── gemini_retry.py
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a root `.env` file with the API keys needed by the notebooks you plan to run.

```text
GOOGLE_API_KEY=your_api_key_here
VOYAGE_API_KEY=your_voyage_api_key_here
```

4. Open the notebooks in VS Code or Jupyter and run cells from top to bottom.

## Dependencies

The project currently depends on:

- `google-genai`
- `tenacity`
- `python-dotenv`
- `pillow`
- `ipython`
- `voyageai`

## Notebook Guide

### Accessing Gemini API

- `make_request.ipynb`: Basic text and image requests, plus token usage display.
- `chat_session.ipynb`: Multi-turn chat sessions with Gemini.
- `chat_exercise.ipynb`: A simple interactive chat exercise.
- `system_prompt.ipynb`: Use of `system_instruction` for role and behavior control.
- `temperature.ipynb`: Single-turn and chat examples with different temperature settings.
- `response_streaming.ipynb`: Streaming model responses.
- `structured_data.ipynb`: JSON mode and schema-based structured output with Pydantic.

### Features of Gemini

- `images.ipynb`: Sends local image data to Gemini and asks the model to perform a fire-risk assessment.
- `pdfs.ipynb`: Uploads a local PDF with the Gemini File API and asks Gemini to summarize the document.
- `citations.ipynb`: Uses File Search to index a PDF, generate grounded answers, parse grounding metadata, and clean up the File Search Store.
- `extended_thinking.ipynb`: Demonstrates a model configured for extended thinking on a complex logic puzzle.

### Prompt Engineering

- `prompting.ipynb`: Baseline prompt engineering and evaluation flow for athlete meal-plan generation.
- `prompting_improved.ipynb`: Improved version of the same workflow with more structured prompting and schema-based grading.

### Prompt Evaluation

- `prompt_evals.ipynb`: Generates an AWS-focused evaluation dataset with a simple chat wrapper.
- `prompt_evals_fns.ipynb`: Builds a full evaluation pipeline with syntax checks and model grading.
- `prompt_evals_complete.ipynb`: Extends the evaluation pipeline with generated grading criteria for each task.

### RAG and Agentic Search

- `chunking.ipynb`: Demonstrates basic text chunking strategies (by character count, by sentence, and by markdown section) using the sample document at `data/chunking.md`.
- `embeddings.ipynb`: Shows how to generate Voyage AI embeddings for section chunks.
- `vectordb.ipynb`: Builds a small in-memory vector index and retrieves chunks by embedding similarity.
- `bm25.ipynb`: Builds a BM25 keyword index for lexical retrieval over the same section chunks.
- `hybrid.ipynb`: Combines BM25 and vector search with reciprocal rank fusion for hybrid retrieval.

### Tool Use with Gemini

- `tool_functions.ipynb`: Demonstrates how to define Python functions as tools, including automatic tool schema generation and model-driven tool calling with Gemini.
- `tool_streaming.ipynb`: Shows how to handle tool calls in a streaming response loop.
- `web_search_tool.ipynb`: Demonstrates Gemini's built-in Google Search grounding tool for retrieving real-time information from the web.
- `text_editor_tool.ipynb`: A complex tool example implementing a filesystem editor with create, view, replace, and undo capabilities. Includes an interactive multi-turn chat mode.

## Playground for Tools

The project root includes a `playground/` directory. This is a safe, isolated area designed for testing tools (like the `TextEditorTool`) that interact with the filesystem. Files created by tools during experimentation will be saved here.

## Retry and Rate Limits

Several notebooks now use a shared retry helper in `utils/gemini_retry.py`.

That helper:

- wraps `client.models.generate_content(...)`
- retries on `429`, `RESOURCE_EXHAUSTED`, and related quota-style failures
- uses exponential backoff through `tenacity`
- re-raises non-rate-limit errors immediately

If you still hit quota or rate-limit failures during dataset generation or evaluation, reduce notebook concurrency first. In the evaluator notebooks, the safest follow-up change is usually lowering `max_concurrent_tasks` to `1`.

## File and Search Resources

The feature notebooks use two different Gemini resource flows:

- `pdfs.ipynb` uploads a file through the File API and passes the uploaded file object directly to the model.
- `citations.ipynb` creates a File Search Store, uploads a PDF into that store, polls the indexing operation, and uses the `file_search` tool for grounded responses.

File Search Stores cannot be deleted while they contain indexed documents unless deletion is forced. The cleanup cell in `citations.ipynb` uses `types.DeleteFileSearchStoreConfig(force=True)` so rerunning the notebook does not leave extra stores behind.

## Generated Outputs

The repository already contains generated artifacts under `data/` and `reports/`.

- `data/` contains datasets and evaluation results produced by the notebooks.
- `reports/` contains generated HTML evaluation reports.

These files can be regenerated by rerunning the corresponding notebooks.

## Suggested Run Order

If you are working through the project end to end, this order is the most coherent:

1. Start with `notebooks/accessing_gemini_api/`
2. Explore `notebooks/features_of_gemini/`
3. Continue with `notebooks/tool_use_with_gemini/`
4. Move to `notebooks/prompt_evaluation/`
5. Finish with `notebooks/prompt_engineering/prompting.ipynb`
6. Then run `notebooks/prompt_engineering/prompting_improved.ipynb`
7. Explore `notebooks/rag_and_agentic_search/chunking.ipynb`
8. Continue through `notebooks/rag_and_agentic_search/embeddings.ipynb`, `vectordb.ipynb`, `bm25.ipynb`, and `hybrid.ipynb`

## Notes

- The notebooks expect the project root to contain `.env` and `requirements.txt`.
- Some notebooks import shared utilities by locating the project root dynamically.
- The PDF and image notebooks expect sample files under `assets/pdfs/` and `assets/images/`.
- The RAG notebooks that generate embeddings require a valid Voyage AI API key.
- Generated notebook outputs may differ depending on your current Gemini model access, quota, and network state.

## Attribution

This project was adapted from course material originally centered on Anthropic API workflows and rewritten here for learning with the Google Gemini SDK.

## Security

Do not commit your `.env` file or API keys. Keep secrets local and private.
