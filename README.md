# Factory Localization Assistant

This repository contains a factory localization assistant application that uses LLM models to summarize and answer questions about documents. The application is built using Streamlit, Langchain and Ollama models.

## Features

- Upload PDF files for summarization and querying.
- Select specific page ranges for processing.
- Choose between summarizing the document or querying specific information.
- Customize criteria for factory location selection.
- Edit and save criteria explanations.
- Display prompts and results.
- Show thinking process of deepseek reasoning model.

## Installation
1. Ensure you have Python 3.12.7 installed. You can download it from the [official Python website](https://www.python.org/downloads/release/python-3127/).

2. Clone the repository:

    ```bash
    git clone https://github.com/sonya2203/factory-localization-assistant
    cd factory-localization-assistant
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Download [Ollama](https://ollama.com/download) (version 0.4.1) and `mistral` and `deepseek-r1:7b` models:

    ```bash
    ollama pull mistral
    ollama pull deepseek-r1:7b
    ```

## Usage
1. Start the Ollama server:

    ```bash
    ollama serve
    ```
2. Run the Streamlit application:

    ```bash
    streamlit run doc_app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the application.

4. Upload a PDF file, select the desired options, and click "Run" to process the document.

## File Structure

- `doc_app.py`: Main application file.
- `criteria_explanation.py`: Contains criteria explanations for factory location selection.
- `st_helpers.py`: Helper functions for Streamlit components.
- `requirements.txt`: List of required Python packages.
