import os
import time
import getpass # পাসওয়ার্ড টাইপ করার সময় তা লুকিয়ে রাখার জন্য

# --- কনফিগারেশন ---
MASTER_PIN = "2026"  # আপনার ডিফল্ট পাসওয়ার্ড (এটি বদলে নিজের মতো সেট করুন)
USER_NAME = "Tareq Shikder"

def clear_screen():
    os.system('clear')

def show_banner():
    print("\033[1;36m" + "="*50)
    print(f"   PINNACLE AI UNIVERSITY - SOVEREIGN HUB   ")
    print(f"   Welcome, Chairman {USER_NAME}            ")
    print("="*50 + "\033[0m")

def login():
    clear_screen()
    show_banner()
    print("\n[!] SECURITY ALERT: Unauthorized Access is Prohibited.")
    
    # getpass ব্যবহার করলে টাইপ করার সময় পাসওয়ার্ড স্ক্রিনে দেখা যাবে না
    attempt = getpass.getpass(f"Enter Sovereign Access Key: ")
    
    if attempt == MASTER_PIN:
        print("\n\033[1;32m[+] Access Granted. Initializing Sovereign Core...\033[0m")
        time.sleep(1.5)
        return True
    else:
        print("\n\033[1;31m[-] Access Denied. Integrity Check Failed.\033[0m")
        time.sleep(2)
        return False

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print("\n1. 🔐 [Core Intelligence] - Manage PQC Vault")
        print("2. 🤖 [Automation Hub] - Start Pixel 7 Tracking")
        print("3. 📑 [Defense Research] - View Strategic Files")
        print("4. 🛡️ [Cyber Fortress] - System Audit & Security")
        print("5. 🚀 [Cloud Sync] - Secure Push to GitHub")
        print("0. 🚪 [Exit] - Secure Logout")
        print("\n" + "-"*50)
        
        choice = input("\033[1;33mSelect Department (0-5): \033[0m")

        if choice == '1':
            print("\n[!] Accessing sovereign_vault.py...")
            time.sleep(2)
        elif choice == '2':
            print("\n[!] Initializing Real-time Data Tracking...")
            time.sleep(2)
        elif choice == '5':
            print("\n[!] Pushing Updates to GitHub...")
            os.system('git add . && git commit -m "System Update via Sovereign Hub" && git push origin master')
            input("\nPress Enter to continue...")
        elif choice == '0':
            print("\n[!] System Secured. Goodbye!")
            break
        else:
            print("\n[!] Invalid Selection.")
            time.sleep(1)

if __name__ == "__main__":
    if login():
        main_menu()
