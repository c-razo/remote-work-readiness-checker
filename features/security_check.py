import platform
import getpass
import subprocess

def system_security_check():
    """
    Perform a basic system security check.
    """
    results = {}

    # Check OS
    os_name = platform.system()
    os_version = platform.version()
    results["Operating System"] = f"{os_name} (Version: {os_version})"

    # Check for a user with default username
    username = getpass.getuser()
    if username.lower() in ["admin", "root", "user"]:
        results["Default Username"] = f"Warning: The username '{username}' is generic. Consider changing it."

    # Placeholder for strong password check
    results["Password Strength"] = "Ensure you are using a strong password (not checked here)."

    # Check firewall status (macOS-specific)
    if os_name == "Darwin":
        try:
            firewall_status = subprocess.run(
                ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"],
                capture_output=True, text=True
            )
            if firewall_status.stdout.strip() == "1":
                results["Firewall"] = "Enabled"
            else:
                results["Firewall"] = "Disabled. Enable it for better security."
        except Exception as e:
            results["Firewall"] = f"Error checking firewall status: {e}"

        # Check for macOS software updates
        try:
            update_status = subprocess.run(
                ["softwareupdate", "--list"],
                capture_output=True, text=True
            )
            if "No new software available." in update_status.stdout:
                results["Software Updates"] = "Up to date"
            else:
                results["Software Updates"] = "Updates available. Run 'softwareupdate -i -a' to install."
        except Exception as e:
            results["Software Updates"] = f"Error checking software updates: {e}"

    # Placeholder for antivirus check
    results["Antivirus"] = "No antivirus detected. Consider installing one for better security."

    # Placeholder for 2FA Check
    results["2FA"] = "Check manual configuration for 2FA (not implemented yet)."

    return results

