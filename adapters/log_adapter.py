import subprocess
import os
from datetime import datetime

IS_DEMO = os.getenv("DEMO_MODE", "false").lower() == "true"

def log_message(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"

    if IS_DEMO:
        with open("demo_logs.txt", "a") as f:
            f.write(full_message + "\n")
        print(f"[DEMO LOG] {full_message}")
    else:
        try:
            result = subprocess.run(
                ["dfx", "canister", "call", "log_canister", "log", f'( "{full_message}" )'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"[LOGGED] {full_message}")
            else:
                print("[ERROR] Logging failed:", result.stderr)
        except Exception as e:
            print("[EXCEPTION] Logging failed:", e)
