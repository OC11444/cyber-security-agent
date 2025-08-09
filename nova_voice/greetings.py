# nova_voice/greetings.py

from datetime import datetime
from tzlocal import get_localzone
from assistant.branding import ASSISTANT_NAME, PROJECT_NAME

def get_greeting():
    local_timezone = get_localzone()
    current_hour = datetime.now(local_timezone).hour

    if current_hour < 12:
        return f"Good morning. I'm {ASSISTANT_NAME}, your {PROJECT_NAME} assistant."
    elif 12 <= current_hour < 18:
        return f"Good afternoon. I'm {ASSISTANT_NAME}, your {PROJECT_NAME} assistant."
    else:
        return f"Good evening. I'm {ASSISTANT_NAME}, your {PROJECT_NAME} assistant."
