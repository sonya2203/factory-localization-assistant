# config/config.py
import os

API_KEY = os.getenv('HUGGING_FACE_API_KEY', 'your key')  # Load from env variable or set a default for testing
API_ENDPOINT = "https://api-inference.huggingface.co/models"  # Base endpoint for Hugging Face Inference API


