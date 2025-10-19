README.md

# 🛡️ Cyber Assistant

A cross-platform terminal assistant designed for ethical hackers, red teamers, and developers. Supports both voice and text input, generates terminal commands using AI (OpenAI/Gemini), explains outputs, and runs securely inside Linux shells.

- **Privacy-first** (offline demo mode available)
- **Debian-ready** (.deb install support)
- **Containerized** (Docker + CI/CD ready)
- **Voice-enabled**
- **ICP-enabled** (WCHL compliance ✅)

---
videos youtube 
first set up:https://youtu.be/n165TtI_aLQ
demo _mode:https://youtu.be/7wr2LCZurDA
live mode:https://youtu.be/i5ATgRiXxxk
live2:https://youtu.be/k3ONRbtxZWc

## 🚀 Features

- Voice or text input interface
- AI-generated shell commands with explanations
- Docker-ready and `.deb` packaged
- Offline mode (no API keys required)
- Canister logging to ICP (WCHL-compliant)
- Parrot/Kali/Ubuntu compatible

---

## 🧠 ICP Integration

This project includes a minimal on-chain component for WCHL compliance.

- Canister: `log_canister` written in Motoko
- File: `src/log_canister/main.mo`
- Usage: Logs events like `"Cyber Assistant launched"` to the Internet Computer console
- Deployed using `dfx`

### 📦 Setup for ICP

1. **Install DFX:**

```bash
sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"

Then restart terminal.

    Start local replica and deploy:

dfx start --background
dfx deploy

    Log a command to the chain:

dfx canister call log_canister log '( "Cyber Assistant launched." )'

🧪 Modes
1. 🧼 Demo Mode (No keys or tools required)

python3 main.py --demo

    Simulates full interaction

    Good for showcasing UX to judges

    Safe to use on any system

2. 🔐 Live Assistant Mode (Real commands)

export OPENAI_API_KEY="your-key"
python3 main.py --model openai

    Will generate and run real commands

    Use inside test environments only



🧩 Folder Structure

cyber-assistant/
├── adapts/              # Text/voice input adapters
├── assistant/           # GPT logic and command generators
├── branding/            # Branding info for multi-platform support
├── src/
│   └── log_canister/    # ICP Motoko canister (main.mo)
├── main.py              # Entry point
├── dfx.json             # ICP project config
├── Dockerfile           # Docker build
├── cyber-assistant.deb  # Debian package (optional)
├── README.md            # You're here!

🧑‍💻 Maintainer

James Njenga — jamesgitau.dev
📜 License

MIT
🏁 WCHL Notes

✅ This project includes:

    dfx.json

    main.mo

    Local canister support

    Demo and full CLI modes
