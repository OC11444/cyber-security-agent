# core/icp.py

import json
import subprocess
from datetime import datetime
from core.command_processor import should_abort_due_to_unsafe_input
from utils.logger import logger

LOG_FILE = "logs/icp_log.jsonl"


def run_secure_command(command: str, secure_mode: bool) -> str:
    """
    Run a shell command securely and log the attempt and output.
    """
    if should_abort_due_to_unsafe_input(command, secure_mode):
        logger.warning(f"[SECURE MODE] Unsafe command blocked: {command}")
        return "[SECURE MODE] Command blocked for safety."

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        logger.info(f"[EXECUTED] {command}")
        log_command_entry(command, output)
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e}")
        log_command_entry(command, str(e))
        return f"[ERROR] {e}"


def log_command_entry(command: str, output: str):
    """
    Logs a command and its output into an immutable log file.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "command": command,
        "output": output.strip()[:1000]  # truncate to prevent leaks
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


def scan_canisters(secure_mode):
    """
    Scans all deployed canisters and returns info.
    """
    logger.info("Scanning all canisters...")
    command = "dfx canister list"
    return run_secure_command(command, secure_mode)


def canister_status(canister_id: str, secure_mode: bool):
    """
    Fetch detailed status of a specific canister.
    """
    logger.info(f"Checking canister: {canister_id}")
    command = f"dfx canister status {canister_id}"
    return run_secure_command(command, secure_mode)


def send_log_to_canister(message: str) -> str:
    """
    Calls the Motoko log canister to log a message.
    """
    logger.info(f"Sending log message to Motoko canister: {message}")
    try:
        result = subprocess.run(
            ['dfx', 'canister', 'call', 'log_canister', 'log', f'("{message}")'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to send log to canister: {e.stderr.strip()}")
        return f"[ERROR] Failed to log to canister: {e.stderr.strip()}"
