assistant/core.py
import os
import sys
import openai
import google.generativeai as genai
from dotenv import load_dotenv
from assistant.branding import PROJECT_NAME  # 🔧 Added for mock branding

load_dotenv()

# 🧪 Check if running in DEMO mode via env (set in main.py)
DEMO_MODE = os.getenv("DEMO_MODE") == "true"

class AIAdapter:
    def __init__(self):
        if DEMO_MODE:
            self.provider = "demo"
            print("[🧪 DEMO] AIAdapter initialized in DEMO mode.")
            return

        self.provider = self.detect_llm()

        if self.provider == "openai":
            openai.api_key = os.getenv("OPENAI_API_KEY")
            if not openai.api_key:
                raise ValueError("OPENAI_API_KEY not found in .env for OpenAI provider.")

        elif self.provider == "gemini":
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                raise ValueError("GEMINI_API_KEY not found in .env for Gemini provider.")
            genai.configure(api_key=gemini_api_key)

        else:
            print("[❌] No valid LLM API key found. Please set GEMINI_API_KEY or OPENAI_API_KEY.")

    def detect_llm(self):
        if os.getenv("OPENAI_API_KEY"):
            return "openai"
        elif os.getenv("GEMINI_API_KEY"):
            return "gemini"
        else:
            return "none"

    def chat_completion(self, messages, model=None, temperature=0.3, max_tokens=400):
        if DEMO_MODE:
           return self.mock_demo_response()

        

        if self.provider == "openai":
            if model is None:
                model = "gpt-4"
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response["choices"][0]["message"]["content"].strip()

        elif self.provider == "gemini":
            if model is None:
                model = "models/gemini-2.5-pro"

            gemini_messages = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                gemini_messages.append({"role": role, "parts": [msg["content"]]})

            model_instance = genai.GenerativeModel(model)
            response = model_instance.generate_content(
                gemini_messages,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=10000,
                ),
            )
            return response.text

        else:
            return "[❌] No valid LLM API key found. Please set GEMINI_API_KEY or OPENAI_API_KEY."

    def list_models(self):
        if DEMO_MODE:
            print("[🧪 DEMO] Model listing skipped in demo mode.")
            return

        if self.provider == "gemini":
            print("Attempting to list Gemini models...")
            for m in genai.list_models():
                print(
                    f"  Name: {m.name}, "
                    f"Supported Generation Methods: {m.supported_generation_methods}"
                )
        else:
            print("Model listing is only implemented for Gemini provider.")

    def mock_demo_response(self):
        return (
            f"[🧪 DEMO] Mock response: Here are 3 fake commands:\n"
        f"1. ls -la\n"
        f"2. whoami\n"
        f"3. ping {PROJECT_NAME.lower()}.local"
    )
        
        
