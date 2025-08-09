# assistant/shell_tools.py

import subprocess
import shutil
import os
import sys

def run_shell_command(command, use_sudo=False):
    """
    Executes a shell command with optional sudo and returns its output or error.

    Args:
        command (str): Shell command to run.
        use_sudo (bool): Whether to prepend 'sudo' if not present.

    Returns:
        str: Output or error message.
    """
    # Add sudo only if it's not already there and use_sudo is requested
    if use_sudo and not command.strip().startswith("sudo"):
        command = f"sudo {command.strip()}"

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()


def is_demo_mode():
    """
    Checks if the system is running in demo mode via CLI flag or environment.

    Returns:
        bool: True if demo mode is active, False otherwise.
    """
    return '--demo' in sys.argv or os.getenv('DEMO_MODE') == '1'


def list_available_tools():
    """
    Lists available hacking tools based on whether in real or demo mode.

    Returns:
        dict: Dictionary with tool names and their availability status.
    """
    tools_to_check = [
        "nmap",
        "sqlmap",
        "john",
        "hydra",
        "msfconsole",
        "nikto",
        "gobuster",
        "rustscan",
        "wpscan",
        "hashcat"
    ]

    if is_demo_mode():
        return {tool: "✔️ (mocked)" for tool in tools_to_check}

    tool_status = {}
    for tool in tools_to_check:
        path = shutil.which(tool)
        tool_status[tool] = f"✔️ ({path})" if path else "❌ Not Found"

    return tool_status


def print_available_tools():
    """
    Prints a user-friendly list of available tools.
    """
    print("🔧 Tool Availability:\n")
    tools = list_available_tools()
    for tool, status in tools.items():
        print(f"• {tool:<12} => {status}")
