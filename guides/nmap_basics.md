

# 🌐 Nmap Basics Guide with CyberGPT Assistant

## What is Nmap?
Nmap ("Network Mapper") is a powerful open-source tool for network discovery and security auditing. It can scan ports, detect services, and map networks — essential for ethical hacking and system hardening.

---

## Using Nmap with Nova (CyberGPT Assistant)

Nova helps you generate and understand Nmap commands from simple questions like:

> "How do I scan open ports on 192.168.1.1?"

Nova will suggest safe commands along with alternatives and explanations — no matter if you're using Ubuntu, Kali, or Parrot OS.

---

## 🔧 Common Nmap Commands

### 1. Simple Port Scan
```bash
nmap 192.168.1.1

2. Version Detection (Services)

nmap -sV 192.168.1.1

3. Scan a Subnet

nmap 192.168.1.0/24

4. Aggressive Scan (More Details)

nmap -A 192.168.1.1

🎤 How to Ask Nova

Try voice or text prompts like:

    "Scan all ports on my local network."

    "Show me services running on 10.0.0.5"

    "Help me do an aggressive scan on 192.168.1.10"

Nova responds with commands + numbered options you can choose from — ready to copy, run, or modify.
⚖️ Ethical Reminder

    ✅ Only scan networks you own or have explicit permission to audit. Unauthorized scanning is illegal and unethical.

💡 Tips

    Use the numbered command menu to choose what to run.

    Ask Nova to explain the command output line by line.

    You can combine flags (like -sV -A) for deeper analysis.