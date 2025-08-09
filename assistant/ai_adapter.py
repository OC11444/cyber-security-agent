import os
import sys
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
DEMO_MODE = "--demo" in sys.argv


class AIAdapter:
    def __init__(self, demo_mode=False):  # ✅ ADDED ARG
        if demo_mode:
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
        if self.provider == "demo":  # ✅ Changed from DEMO_MODE to self.provider
            return "[🧪 DEMO] Mock LLM response: This is where your 3 fake commands would appear."

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
        if self.provider == "demo":
            print("[🧪 DEMO] Skipping model list in demo mode.")
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


# ✅ Add this so main.py can use: from ai_adapter import ask_gpt
def ask_gpt(messages, model=None, temperature=0.3, max_tokens=400):
    adapter = AIAdapter(demo_mode=DEMO_MODE)
    return adapter.chat_completion(messages, model=model, temperature=temperature, max_tokens=max_tokens)
