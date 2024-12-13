from pathlib import Path
from typing import List
import streamlit as st

from .document import load_pdf
from .query import query_document
from .summarize import summarize_document


def save_uploaded_files(
    uploaded_files: List["UploadedFile"], output_dir: Path = Path("/tmp")
) -> List[Path]:
    saved_paths = []
    for uploaded_file in uploaded_files:
        output_path = Path(output_dir) / uploaded_file.name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        saved_paths.append(output_path)
    return saved_paths


def run_query(
    uploaded_files: List["UploadedFile"],
    summarize: bool,
    user_query: str,
    start_page: int,
    end_page: int,
    model_name: str,
    openai_api_key: str,
    openai_url: str,
    temperature: float,
    criteria_explanations_text: str,
) -> List[str]:
    results = []
    # Saves the uploaded file to a temporary location, loads the PDF, and deletes the file
    st.write("Saving the uploaded file...")
    file_paths = save_uploaded_files(uploaded_files, output_dir=Path("/tmp"))
    
    for uploaded_file,file_path in zip(uploaded_files,file_paths):
        st.write(f"Loading the document {uploaded_file.name}...")
        docs = load_pdf(file_path, start_page=start_page, end_page=end_page)
        file_path.unlink()
        if summarize:
            st.write(f"Summarizing the document {uploaded_file.name}...")
            prompt, summary = summarize_document(docs, model_name, openai_api_key, openai_url, temperature)
            results.append(f"Summary of {uploaded_file.name}: {summary}")
        else:
            st.write(f"Querying the document {uploaded_file.name}...")
            map_prompt, reduce_prompt, answer = query_document(docs, user_query, model_name, openai_api_key, openai_url, temperature, criteria_explanations_text)
            prompt = f"Map prompt: {map_prompt}\nReduce prompt: {reduce_prompt}"
            results.append(f"Answer from {uploaded_file.name}: {answer}")
    return prompt, results