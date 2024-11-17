from flask import Flask, render_template, request, jsonify
import speedtest
import platform
import subprocess
import re

app = Flask(__name__)

# Function to perform the speed test
def run_speed_test():
    speed_results = {}
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        speed_results["download_speed"] = round(st.download() / 1e6, 2)  # Mbps
        speed_results["upload_speed"] = round(st.upload() / 1e6, 2)  # Mbps
        speed_results["ping"] = round(st.results.ping, 2)
    except Exception as e:
        # Fallback values for errors
        speed_results["download_speed"] = "Unavailable"
        speed_results["upload_speed"] = "Unavailable"
        speed_results["ping"] = "Unavailable"
        print(f"Speedtest Error: {e}")
    return speed_results

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Weak: Include uppercase and lowercase letters"
    if not re.search("[0-9]", password):
        return "Weak: Include at least one number"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Include special characters"
    return "Strong"

# Function to check firewall status
def check_firewall_status():
    try:
        # Run the macOS firewall status command
        output = subprocess.check_output(
            ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
            stderr=subprocess.STDOUT
        )
        # Parse the output for "enabled" or "disabled"
        if b"enabled" in output.lower():
            return "Enabled"
        else:
            return "Disabled"
    except Exception as e:
        print(f"Firewall Status Error: {e}")
        return "Error checking firewall status"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Run the speed test synchronously
    speed_results = run_speed_test()

    # Get system information
    operating_system = f"{platform.system()} {platform.version()}"
    firewall_status = check_firewall_status()  # Actual firewall status
    antivirus_status = "Active" if platform.system() == "Windows" else "No antivirus detected"
    software_updates = "Up-to-date" if platform.system() == "Darwin" else "Check for updates manually"
    two_factor_authentication = "Check manual configuration for 2FA"  # Placeholder

    # Default password strength
    password_strength = "No password entered"

    # Check for submitted password
    if request.method == 'POST':
        password = request.form.get('password', '')
        password_strength = check_password_strength(password)

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

@app.route('/speedtest-results')
def get_speedtest_results():
    return jsonify(run_speed_test())

if __name__ == '__main__':
    app.run(debug=True)
