import logging

logger = logging.getLogger("cyber-sec-agent")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(console_handler)

