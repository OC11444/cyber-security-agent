import re
from core.icp import scan_canisters, canister_status
from utils.logger import logger
from core.icp import send_log_to_canister


def handle_icp_command(user_input: str, secure_mode: bool = True) -> str:
    """
    Maps user input to appropriate ICP actions.
    """
    user_input = user_input.lower().strip()

    if "scan" in user_input and "canister" in user_input:
        logger.info("Routing to scan_canisters")
        return scan_canisters(secure_mode)
    
    if "status" in user_input and "canister" in user_input:
        canister_id_match = re.search(r"\b[a-z0-9-]{5,}\b", user_input)
        if canister_id_match:
            canister_id = canister_id_match.group()
            logger.info(f"Routing to canister_status for {canister_id}")
            return canister_status(canister_id, secure_mode)
        return "[ERROR] Canister ID not found in command."

    if "log" in user_input:
        log_match = re.search(r"log\s+(.*)", user_input)
        if log_match:
            log_message = log_match.group(1)
            logger.info(f"Routing log message to canister: {log_message}")
            from core.icp import send_log_to_canister
            return send_log_to_canister(log_message)
        return "[ERROR] No log message provided."

    return "[ERROR] ICP command not recognized."
