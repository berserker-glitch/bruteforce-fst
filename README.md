````markdown
# 🔐 APOGE Birthdate Brute-force Tool

A Python script to brute-force birthdates for the student portal of [apoweb-te.uae.ac.ma](https://apoweb-te.uae.ac.ma/dossier_etudiant_fs_tetouan/), using a known APOGE code and a range of dates within a year.

> ⚠️ **DISCLAIMER**: This tool is for educational and ethical research purposes only. Unauthorized access or use without permission is illegal.

---

## 📦 Features

- Tries all possible birthdates in a given year for a specific Apoge code.
- Saves successfully discovered credentials.
- Opens browser via Selenium for quick manual access if login is successful.
- Provides clean logging and user interaction.

---

## ✅ Requirements

- Python 3.7 or later
- Google Chrome browser
- ChromeDriver installed and in system PATH

### Install Dependencies

```bash
pip install requests selenium urllib3
````

---

## 🚀 Usage

1. Ensure ChromeDriver is installed.
2. Run the script:

```bash
python apoge_bruteforce.py
```

3. Follow the prompts:

   * Enter the 8-digit Apoge code.
   * If credentials are saved, auto-login via browser.
   * Otherwise, enter a year to try all birthdates from January 1 to December 31.

---

## 🗂️ Output

* Successful login credentials are stored in `credentials.txt` in this format:

```
12345678:01/02/2001
```

* The browser auto-opens and logs in using Selenium.

---

## 🔒 Ethical Notice

This script should **only** be used with proper authorization. Do **not** run this tool on systems you do not own or have explicit permission to test.

---

## 🧠 Example

```text
🔥 APOGE BIRTHDATE BRUTEFORCE TOOL
💻 Developed for apoweb-te.uae.ac.ma

🔐 Enter 8-digit Apoge code: 12345678
📅 Enter birth year to try (or type 'exit' to quit): 2001

>>> Starting bruteforce for year 2001...

🔍 Trying 01/01/2001
...
✅ SUCCESS ➜ Birthdate found: 05/03/2001
🌐 Opening browser and logging in...
✅ Submitted login form.
🖱️ Clicked 'Licence'
🖱️ Clicked 'Afficher'
```

---

## ⚖️ License

No license provided. Intended for personal academic use only. Do not redistribute or use for malicious purposes.

