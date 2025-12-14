# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI + HTMX sample application that demonstrates real-time LLM text generation using Ollama. The application uses HTMX for dynamic content updates without requiring JavaScript, making it a minimal yet functional prototype for AI-powered text generation.

## Development Environment

- **Python Version**: >=3.13
- **Package Management**: uv (commands: `uv add`, `uv run`)
- **Dependencies**: FastAPI, Jinja2, HTMX (via CDN), Uvicorn, Requests

## Running the Application

Start the development server:
```bash
uv run uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## Architecture

### Application Flow
1. User accesses root `/` → renders [index.html](templates/index.html) via Jinja2
2. User submits form → HTMX posts to `/generate` endpoint
3. Backend calls Ollama API (localhost:11434) with the prompt
4. Response is streamed back as HTML fragment and injected into `#result` div

### Key Components
- **[main.py](main.py)**: Single-file FastAPI application
  - `/` (GET): Serves the main HTML page
  - `/generate` (POST): Handles form submission and Ollama API integration
- **[templates/index.html](templates/index.html)**: Jinja2 template with HTMX directives
  - Uses HTMX attributes (`hx-post`, `hx-target`) for dynamic updates
  - HTMX loaded from CDN (v1.9.10)

### External Dependencies
- **Ollama**: Must be running locally on port 11434
- **Model**: Configured to use `gpt-oss:20b` (see `OLLAMA_MODEL` in [main.py](main.py))

## Configuration

Ollama settings are hardcoded in [main.py](main.py:11-12):
- `OLLAMA_URL`: http://localhost:11434/api/generate
- `OLLAMA_MODEL`: gpt-oss:20b

To use a different model or endpoint, modify these constants.
