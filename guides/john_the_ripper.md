

# 🔐 John the Ripper Basics Guide

## 🧠 What is John the Ripper?

John the Ripper is a powerful password cracking tool used to test password strength by brute force, dictionary attacks, and more. It supports a wide range of hash formats and can be used in offline ethical password audits.

---

## ⚙️ Installation

**Linux (Debian-based):**
```bash
sudo apt update && sudo apt install john

macOS (with Homebrew):

brew install john

Windows:
Download from the official repository: https://www.openwall.com/john/
🚀 Common Commands
1. Crack hashes from a file

john hashes.txt

<!-- [ADD SCREENSHOT: Terminal showing john cracking a hash file] -->
2. Use a custom wordlist

john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

<!-- [ADD SCREENSHOT: Terminal showing john using a wordlist] -->
3. View cracked passwords

john --show hashes.txt

<!-- [ADD SCREENSHOT: Terminal showing cracked passwords] -->
🗣️ How to Ask the Assistant (UX Example Prompts)

Ask the assistant things like:

    “Crack password hashes from file.”

    “Use a wordlist with John the Ripper.”

    “Show cracked passwords.”

    “What are the hash types supported by John?”

The assistant will suggest:

    ✅ Command options (numbered)

    🧠 Clear explanations of each

    💬 Simulated outputs in DEMO mode

⚠️ Ethical Notice

Only crack hashes that you have legal and ethical permission to test. Unauthorized password cracking is illegal.
🧩 Pro Tips

    Use --format=FORMAT to specify hash types (e.g., --format=md5)

    Combine with hashid or hash-identifier to detect hash types before cracking

    Add --session for pause/resume cracking sessions

💡 UI/UX Suggestions

If you're building a front-end or CLI around this:

    Show progress bars (cracking... 43%)

    Let users upload hash files or paste hashes

    Provide dropdowns for selecting wordlists

    Use tooltips to explain command flags