# Factory Localization Assistamt

This repository contains a factory localization assistant application that uses LLM models to summarize and answer questions about documents. The application is built using Streamlit, Langchain and Ollama models.

## Features

- Upload PDF files for summarization and querying.
- Select specific page ranges for processing.
- Choose between summarizing the document or querying specific information.
- Customize criteria for factory location selection.
- Edit and save criteria explanations.
- Display prompts and results.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sonya2203/factory-localization-assistant
    cd factory-localization-assistant
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your OpenAI API key and other necessary environment variables. Please also change the path pointing to the environment in `doc_app.py`:

    ```env
    OPENAI_URL = "http://localhost:11434/v1"
    OPENAI_API_KEY = "ollama"
    MODEL_NAME = "mistral"
    ```
5. Download Ollama (https://ollama.com/download) and mistral model:

    ```bash
    ollama pull mistral
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run doc_app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

3. Upload a PDF file, select the desired options, and click "Run" to process the document.

## File Structure

- `doc_app.py`: Main application file.
- `criteria_explanation.py`: Contains criteria explanations for factory location selection.
- `st_helpers.py`: Helper functions for Streamlit components.
- `requirements.txt`: List of required Python packages.
- `.env`: Environment variables file (not included in the repository).
