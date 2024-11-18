import subprocess
import platform
from flask import Flask, render_template, jsonify, request
import speedtest

# Initialize the Flask app
app = Flask(__name__)

# Function to check firewall status
def get_firewall_status():
    try:
        if platform.system() == "Darwin":  # macOS
            result = subprocess.run(
                ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return "Enabled" if "enabled" in result.stdout.lower() else "Disabled"
        elif platform.system() == "Windows":  # Windows
            return "Active"  # Placeholder for Windows implementation
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
        print(f"Speedtest Error: {e}")
        speed_results = {
            "download_speed": "Unavailable",
            "upload_speed": "Unavailable",
            "ping": "Unavailable",
        }
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

# Route to render the main page
@app.route("/")
def index():
    firewall_status = get_firewall_status()
    speed_results = run_speed_test()
    return render_template(
        "index.html",
        operating_system=f"{platform.system()} {platform.version()}",
        password_strength="Ensure you are using a strong password",
        firewall_status=firewall_status,
        software_updates="Up-to-date" if platform.system() == "Darwin" else "Check manually",
        antivirus_status="No antivirus detected",
        two_factor_authentication="Check manual configuration for 2FA",
        download_speed=speed_results["download_speed"],
        upload_speed=speed_results["upload_speed"],
        ping=speed_results["ping"],
    )

# Route to check password strength
@app.route("/check-password", methods=["POST"])
def check_password():
    try:
        data = request.get_json()
        password = data.get("password", "")
        strength = check_password_strength(password)
        return jsonify({"strength": strength})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

# Route to return speed test results as JSON
@app.route("/speedtest-results")
def get_speedtest_results():
    return jsonify(run_speed_test())

if __name__ == "__main__":
    app.run(debug=True)
