# 🧠 Assistant Core Logic

This directory contains the core logic that powers the **Assistant** — including LLM interaction handlers, shell command analysis, and decision-making layers. It serves as the brain of the assistant, coordinating inputs, responses, and shell execution.

---

## 📁 File Overview

| File                | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| `core.py`           | The central assistant controller: routes input, invokes GPT handler, interprets output, and triggers actions. |
| `openai_handler.py` | Interfaces with OpenAI models (e.g. GPT-3.5 / GPT-4). Includes fallback and structured prompt handling. |
| `gemini_handler.py` | Interfaces with Google's Gemini models. Supports model chaining or fallback if preferred model fails. |
| `shell_tools.py`    | Extracts shell commands from LLM replies, validates them, and executes securely. |
| `ai_adapter.py`     | Adapter logic to abstract away LLM-specific quirks and standardize input/output. |
| `r1_handler.py`     | Handles ranked responses (e.g. Top 3 commands). Provides selection logic for user to choose preferred action. |
| `__init__.py`       | Package initializer.

---

## 🧩 Key Concepts

### 🔁 Model Switching & Fallback
- `core.py` calls `ai_adapter.py`, which delegates requests to either OpenAI or Gemini depending on:
  - Config preference
  - Failures (e.g. API timeouts, null responses)

### 🔎 Shell Command Extraction
- LLM output is parsed for safe, executable shell commands via `shell_tools.py`.
- Validity checks ensure output doesn’t break the system.
- Command explanation is generated using the same LLM after execution.

### 🧠 Decision Ranking
- `gemini_handler.py` processes the LLM output into **ranked command choices**.
- User is prompted to pick a preferred command via numbered selection.
- Example:
  ```bash
  🤖 Choose 1 to run, or type '2' for another:
  1. nmap -sV 127.0.0.1
  2. sudo nmap -A 127.0.0.1
  3. rustscan -a 127.0.0.1 -- -sV -sC

🛠️ Adding a New LLM Handler

To support a new model:

    Create new_model_handler.py.

    Expose ask_model(prompt: str) inside it.

    Add logic inside ai_adapter.py:

    if model_name == "new_model":
        return new_model_handler.ask_model(prompt)

🔄 Assistant Logic Flow

graph TD;
    A[User Input (Voice or Text)] --> B[core.py];
    B --> C[ai_adapter.py];
    C --> D{Choose LLM};
    D -->|Gemini| E[gemini_handler.py];
    D -->|OpenAI| F[openai_handler.py];
    E & F --> G[LLM Response];
    G --> H[shell_tools.py: Extract Commands];
    H --> I[r1_handler.py: Rank Options];
    I --> J[User selects command];
    J --> K[Command executed + explained];

✅ Example Use (Developer Testing)

from assistant.core import run_assistant

response = run_assistant("Scan this IP 192.168.1.1")
print(response)

🧪 Tests

Run relevant logic tests using:

pytest tests/test_core.py

📌 Notes

    These files do not handle voice or audio output — see nova_voice/ or voice_input.py.

    Avoid placing any API keys in this folder; use environment variables or the root .env if needed.

📁 Scope

This logic is modular and built for:

    Easy swapping between models (Gemini ↔ GPT)

    Ranked suggestions and controlled shell execution

    Future upgrades (e.g. Claude, Mistral, local LLMs)