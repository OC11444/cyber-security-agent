# openai_handler.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_openai_response(prompt: str) -> str:
    """
    Sends a prompt to OpenAI and returns the response.

    Args:
        prompt (str): User prompt.

    Returns:
        str: LLM response or error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"
# openai_handler.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_openai_response(prompt: str) -> str:
    """
    Sends a prompt to OpenAI and returns the response.

    Args:
        prompt (str): User prompt.

    Returns:
        str: LLM response or error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"
