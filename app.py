import subprocess
import platform
from flask import Flask, render_template, jsonify, request
import speedtest

app = Flask(__name__)

# Function to check firewall status
def get_firewall_status():
    try:
        if platform.system() == "Darwin":
            # Check firewall status on macOS
            result = subprocess.run(
                ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if "enabled" in result.stdout.lower():
                return "Enabled"
            else:
                return "Disabled"
        elif platform.system() == "Windows":
            # Placeholder for Windows firewall check implementation
            return "Active"  # Placeholder
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error checking firewall: {e}")
        return "Error checking status"

# Function to perform speed test
def run_speed_test():
    speed_results = {}
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        speed_results["download_speed"] = round(st.download() / 1e6, 2)  # Mbps
        speed_results["upload_speed"] = round(st.upload() / 1e6, 2)  # Mbps
        speed_results["ping"] = round(st.results.ping, 2)
    except Exception as e:
        speed_results["download_speed"] = "Unavailable"
        speed_results["upload_speed"] = "Unavailable"
        speed_results["ping"] = "Unavailable"
        print(f"Speedtest Error: {e}")
    return speed_results

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif not any(char.isdigit() for char in password):
        return "Moderate"
    elif not any(char.isupper() for char in password):
        return "Strong"
    else:
        return "Very Strong"

@app.route('/')
def index():
    # Get firewall status
    firewall_status = get_firewall_status()

    # Run speed test
    speed_results = run_speed_test()

    # Placeholder data for now
    operating_system = f"{platform.system()} {platform.version()}"
    password_strength = "Ensure you are using a strong password"
    software_updates = "Up-to-date" if platform.system() == "Darwin" else "Check manually"
    antivirus_status = "No antivirus detected"
    two_factor_authentication = "Check manual configuration for 2FA"

    return render_template(
        'index.html',
        operating_system=operating_system,
        password_strength=password_strength,
        firewall_status=firewall_status,
        software_updates=software_updates,
        antivirus_status=antivirus_status,
        two_factor_authentication=two_factor_authentication,
        download_speed=speed_results["download_speed"],
        upload_speed=speed_results["upload_speed"],
        ping=speed_results["ping"]
    )

@app.r
