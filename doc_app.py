import os
import time

import streamlit as st
from dotenv import load_dotenv
from documents_llm import criteria_explanation
from documents_llm.st_helpers import run_query

# Load environment variables
#USERS: Change the path to the .env file to the path where you have saved the .env file
load_dotenv(dotenv_path='/Users/i749910/ollama-summarizer/.env')

# Load model parameters
MODEL_NAME = os.getenv("MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = os.getenv("OPENAI_URL")

st.title("Factory location selection assistant 🏭")
st.write(
    "This is a document analyzer that uses LLM models to summarize and answer questions about documents. "
    "You can upload a PDF and the model will summarize the document and answer questions about it."
)

with st.sidebar:
    st.header("Model")

    model_name = st.text_input("Model name", value=MODEL_NAME)

    st.header("Temperature", help="Temperature controls the randomness of the model's output. Lower values make the output more deterministic.")
    temperature = st.slider("Temperature",value=0.1, min_value=0.0, max_value=1.0)
    

    st.header("Document")
    st.subheader("Upload a PDF file")
    file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if file:
        st.write("File uploaded successfully!")

    st.subheader("Page range")

    st.write(
        "Select page range. Pages are numbered starting at 0. For end page, you can also use negative numbers to count from the end, e.g., -1 is the last page, -2 is the second to last page, etc."
    )
    col1, col2 = st.columns(2)
    with col1:
        start_page = st.number_input("Start page:", value=0, min_value=0)
    with col2:
        end_page = st.number_input("End page:", value=-1)


    st.subheader("Query type")

    query_type = st.radio("Select the query type", ["Summarize", "Query"])

    st.subheader("Factory Location Criteria")
    criteria = {
        "Economic Feasibility": st.checkbox("Economic Feasibility"),
        "Infrastructure and Accessibility": st.checkbox("Infrastructure and Accessibility"),
        "Environmental Sustainability": st.checkbox("Environmental Sustainability"),
        "Labor Market and Workforce": st.checkbox("Labor Market and Workforce"),
        "Proximity and Logistics": st.checkbox("Proximity and Logistics"),
        "Legal and Political": st.checkbox("Legal and Political"),
        "Growth and Scalability": st.checkbox("Growth and Scalability"),
        "Innovation and Technological Ecosystem": st.checkbox("Innovation and Technological Ecosystem"),
    }

    st.subheader("Custom Criteria")
    custom_criteria = st.text_input("Add custom criteria. Phrase it as a request for an assistant.")


selected_criteria = [
    explanation for criterion, explanation in criteria_explanation.criteria_explanation.items() if criteria[criterion]
]
criteria_explanations_text = "\n".join(selected_criteria) if selected_criteria else "" 
if custom_criteria:
    criteria_explanations_text += "\n" + custom_criteria

if query_type == "Query":
    user_query = st.text_area(
        "User query", value="What is the data used in this analysis?"
    )


if st.button("Run"):
    result = None
    start = time.time()
    if file is None:
        st.error("Please upload a file.")
    else:
        with st.status("Running...", expanded=True) as status:
            try:
                prompt, result = run_query(
                    uploaded_file=file,
                    summarize=query_type == "Summarize",
                    user_query=user_query if query_type == "Query" else "",
                    start_page=start_page,
                    end_page=end_page,
                    model_name=MODEL_NAME,
                    openai_api_key=OPENAI_API_KEY,
                    openai_url=OPENAI_URL,
                    temperature=temperature,
                    criteria_explanations_text=criteria_explanations_text,
                )
                status.update(label="Done!", state="complete", expanded=False)

            except Exception as e:
                status.update(label="Error", state="error", expanded=False)
                st.error(f"An error occurred: {e}")
                result = ""

        if result:
            with st.container(border=True):
                st.header("Prompt")
                st.markdown(prompt)
                st.header("criteria_explanations_text")
                st.markdown(criteria_explanations_text)
                st.header("Result")
                st.markdown(result)
                st.info(f"Time taken: {time.time() - start:.2f} seconds", icon="⏱️")
