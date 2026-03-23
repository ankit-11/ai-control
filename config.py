import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def setup_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.5-flash')