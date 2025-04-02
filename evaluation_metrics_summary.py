import time
from langchain_community.document_loaders.pdf import PyPDFLoader
from sentence_transformers import SentenceTransformer, util
from bert_score import score
import config
import os
# Load the model for embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Set up Hugging Face API token if required
os.environ['HF_HUB_ENABLE_OFFLINE'] = '1'

# Function to evaluate summary quality
def evaluate_summary(pdf_file_path: str, summary_text: str) -> dict:
    start_time = time.time()

    # Extract text from the PDF using PyPDFLoader
    loader = PyPDFLoader(pdf_file_path)
    pages = loader.load()
    pdf_text = '\n'.join([page.page_content for page in pages])

    # Compute BERTScore
    P, R, F1 = score([summary_text], [pdf_text], lang='en')
    bert_score = F1.mean().item()

    # Compute Cosine Similarity
    pdf_embedding = embedding_model.encode(pdf_text, convert_to_tensor=True)
    summary_embedding = embedding_model.encode(summary_text, convert_to_tensor=True)
    cosine_sim = util.cos_sim(summary_embedding, pdf_embedding).item()

    # Processing time
    processing_time = time.time() - start_time

    # Return results as a dictionary
    return {
        'BERTScore': bert_score,
        'Cosine Similarity': cosine_sim,
        'Processing Time': processing_time
    }

# Example usage
if __name__ == '__main__':
    pdf_file_path = 'Logistics-and-Industrial-Market-Overview-JLL-Germany.pdf'
    summary_text = ''' The provided text is a research report on the German logistics and industrial market for the second half of 2022, published by Jones Lang LaSalle (JLL). Here's a summary of the key points:
1.	Increased demand for warehousing space due to e-commerce growth and supply chain disruptions caused by the pandemic.
2.	Rising rents and construction costs in major cities like Berlin, Düsseldorf, Frankfurt, Hamburg, Cologne, Munich, Stuttgart, and Ruhr Area.
3.	Strong investment activity in the industrial sector, with Berlin, Düsseldorf, and Frankfurt being the most active markets.
4.	The report highlights that the logistics and industrial market is expected to remain strong due to ongoing e-commerce growth and supply chain resilience efforts.
5.	JLL provides contact information for their experts in Industrial Leasing, Industrial Investment, and Research, should readers have any questions or suggestions regarding the Logistics and Industrial Market Overview.
6.	The report concludes with a brief introduction to JLL, a leading professional services firm specializing in real estate and investment management. They emphasize their commitment to protecting personal information and offer contact details for further inquiries.

 '''
    results = evaluate_summary(pdf_file_path, summary_text)
    print(results)
