import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def get_ai_response(query: str) -> str:
    return model.generate_content('query').text
