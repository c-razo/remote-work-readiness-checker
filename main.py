PREMIUM_MODE = False  # Set to True to enable premium features

def is_premium():
    if PREMIUM_MODE:
        return True
    else:
        print("\nPremium features are locked. Upgrade to access detailed reports.")
        return False

def prompt_premium_upgrade():
    global PREMIUM_MODE
    user_input = input("Do you want to enable premium mode for enhanced features? (yes/no): ").strip().lower()
    if user_input == 'yes':
        PREMIUM_MODE = True
        print("Premium mode enabled!")
    else:
        print("Continuing in free mode.")

from features.security_check import system_security_check
from features.speed_test import internet_speed_test

if __name__ == "__main__":
    prompt_premium_upgrade()
    
    print("\nRunning System Security Check...")
    security_results = system_security_check()
    for key, value in security_results.items():
        print(f"{key}: {value}")

    # Enhanced Security Report for Premium
    if is_premium():
        print("\n[Premium Feature] Enhanced Security Report:")
        print("- Recommended: Ensure OS patches are up-to-date and use a VPN for secure browsing.")

    print("\nRunning Internet Speed Test...")
    speed_results = internet_speed_test()
    for key, value in speed_results.items():
        print(f"{key}: {value}")

    # Detailed Speed Analysis for Premium
    if is_premium():
        print("\n[Premium Feature] Detailed Speed Analysis:")
        print("- Recommended download speed for HD video calls: 3-4 Mbps or higher.")
        print("- Recommended upload speed for smooth remote work: 1-2 Mbps or higher.")

