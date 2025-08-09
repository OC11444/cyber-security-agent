# core/command_processor.py

import re
from core.secure_mode import is_command_safe
from utils.logger import logger

def extract_shell_command(user_input: str) -> str:
    command_match = re.match(r"run\s+(.*)", user_input.strip(), re.IGNORECASE)
    return command_match.group(1) if command_match else user_input.strip()

def should_abort_due_to_unsafe_input(user_input: str, secure_mode: bool) -> bool:
    extracted = extract_shell_command(user_input)
    if secure_mode and not is_command_safe(extracted):
        logger.warning("[🚫 SECURE MODE] Unsafe input detected. Aborting suggestions.")
        print("[🚫 SECURE MODE] Unsafe input detected. Aborting suggestions.")
        return True
    return False
