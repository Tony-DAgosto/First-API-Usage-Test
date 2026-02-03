import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("API key successfully loaded!" if openai.api_key else "Warning: API key not found!")

