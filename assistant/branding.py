# assistant/branding.py

# Centralized branding info for cross-platform compatibility
PROJECT_DIR_NAME = "parrot-gpt-assistant"

PROJECT_NAME = "CyberGPT"
DESCRIPTION = "Your Cybersecurity Assistant for Linux"
OS_NAME = "Linux"
ASSISTANT_NAME = "Nova"
VOICE_GREETING = f"I'm {ASSISTANT_NAME}, your {PROJECT_NAME} assistant."

# Session-based flag to avoid repeated printing
_greeting_spoken = False

def print_brand():
    global _greeting_spoken
    if _greeting_spoken:
        return  # Don't print again
    _greeting_spoken = True

    print(f"\n🚀 {PROJECT_NAME} - {DESCRIPTION} ({OS_NAME})")
    print(f"🤖 {VOICE_GREETING}\n")
