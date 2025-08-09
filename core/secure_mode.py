# core/secure_mode.py

import re

# Optional: This can be injected dynamically from main.py
ENABLED = False

UNETHICAL_KEYWORDS = [
    "msfvenom",
    "sqlmap",
    "exploit",
    "reverse_shell",
    "netcat -e",
    "bash -i",
    "hydra -L",
    "payload",
    "nc -e",
    "shell_reverse",
    "curl http",
    "wget http",
    "base64 -d",
    "rm -rf /",
    "dd if=",
    "mkfs",
    "format c:"
]

UNSAFE_COMMAND_PATTERNS = [
    r"\brm\s+-rf\s+/",
    r":\s*!rm",
    r"\bshutdown\b",
    r"\breboot\b",
    r"\bmkfs\b",
    r":\s*!dd",
    r"\bpoweroff\b",
    r"\bhalt\b",
    r"\binit\s+0\b",
    r"\b:(){:|:&};:\b",  # fork bomb
]


def filter_unethical_commands(command: str) -> bool:
    """
    Check if the command contains any unethical or dangerous patterns.
    Returns True if the command is allowed (safe), False otherwise.
    """
    lowered = command.lower()
    for keyword in UNETHICAL_KEYWORDS:
        if keyword in lowered:
            return False
    return True


def explain_rejection(command: str) -> str:
    """
    Provide feedback on why a command was rejected.
    """
    for keyword in UNETHICAL_KEYWORDS:
        if keyword in command.lower():
            return f"⚠️ Command blocked by Secure Mode: Detected keyword `{keyword}`"
    return "⚠️ Command blocked by Secure Mode due to unknown violation."


def is_command_safe(command: str) -> bool:
    return not is_unsafe(command)


def is_unsafe(command: str) -> bool:
    for pattern in UNSAFE_COMMAND_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True
    return False
