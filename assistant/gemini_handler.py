# gemini_handler.py

import os
import google.generativeai as genai

# Configure using key from .env
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Preferred models
PREFERRED_MODELS = ["gemini-1.5-pro", "gemini-1.5-flash"]

# Cache model
_model = None


def get_available_model():
    """
    Scans for preferred Gemini models and returns the first usable one.
    """
    print("🔍 Scanning for available Gemini models...")
    for model in genai.list_models():
        if "generateContent" in model.supported_generation_methods:
            if any(pref in model.name for pref in PREFERRED_MODELS) and "vision" not in model.name.lower():
                print(f"[✔️] Using preferred model: {model.name}")
                return genai.GenerativeModel(model.name)
    raise Exception("❌ No usable Gemini model found.")


def get_gemini_response(prompt: str) -> str:
    """
    Uses Gemini to respond to a given prompt. Falls back to 1.5-flash on failure.

    Args:
        prompt (str): The prompt string.

    Returns:
        str: LLM's response or error message.
    """
    global _model
    try:
        if not _model:
            _model = get_available_model()

        response = _model.generate_content(prompt)
        return response.text

    except Exception as e:
        err_str = str(e)

        # Check for quota/rate limit and fallback
        if "429" in err_str or "quota" in err_str.lower():
            print("[⚠️] Gemini quota exceeded. Trying fallback...")
            try:
                fallback = genai.GenerativeModel("models/gemini-1.5-flash")
                response = fallback.generate_content(prompt)
                return response.text
            except Exception as fallback_error:
                return f"[Gemini Fallback Error] {str(fallback_error).splitlines()[0]}"
        else:
            return f"[Gemini Error] {err_str.splitlines()[0]}"
