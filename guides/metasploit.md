

# 🛠️ Metasploit Basics Guide with the GPT Assistant

## What is Metasploit?

Metasploit is a powerful penetration testing framework used to find, exploit, and validate vulnerabilities. It contains a wide range of exploits, payloads, and auxiliary modules.

---

## Using Metasploit with the GPT Assistant

The assistant can help you construct Metasploit commands and guide you through using common modules. For example, you can ask:

> "How do I start Metasploit and run a basic exploit?"

It will suggest commands and explain their usage step-by-step.

---

## Common Metasploit Commands

### 1. Start the Metasploit console
```bash
msfconsole

<!-- [ADD SCREENSHOT: Assistant suggesting msfconsole command] -->
2. Search for an exploit

search vsftpd

<!-- [ADD SCREENSHOT: Assistant suggesting search command] -->
3. Use an exploit module

use exploit/unix/ftp/vsftpd_234_backdoor

<!-- [ADD SCREENSHOT: Assistant showing 'use' command suggestion] -->
4. Set required options (e.g., target IP)

set RHOST 192.168.1.10

<!-- [ADD SCREENSHOT: Assistant suggesting set command] -->
5. Run the exploit

exploit

<!-- [ADD SCREENSHOT: Assistant suggesting exploit command] -->
How to Ask the Assistant

Examples:

    "Open Metasploit console"

    "Search for ftp exploits"

    "Use vsftpd backdoor exploit"

    "Set target IP to 10.0.0.5"

    "Run exploit"

The assistant will reply with suggested commands and clear explanations.
Ethical Reminder

Only use Metasploit against systems you are authorized to test.
Tips

    Use help inside msfconsole to see detailed module options.

    Combine Metasploit with Nmap scans to gather better information on targets.