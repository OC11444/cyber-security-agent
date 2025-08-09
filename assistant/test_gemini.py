# test_gemini.py

from assistant.gemini_handler import get_gemini_response
from dotenv import load_dotenv
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
load_dotenv()

prompt = "What is the difference between TCP and UDP in computer networking?"
print("✅ GEMINI_API_KEY:")
print("🧠 Prompting Gemini...")

response = get_gemini_response(prompt)
print("[Gemini Response]\n", response)
