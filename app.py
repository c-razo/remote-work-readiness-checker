from flask import Flask, render_template, jsonify
import speedtest
import platform
import subprocess

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

# Function to check firewall status
def check_firewall_status():
    try:
        if platform.system() == "Darwin":  # macOS
            result = subprocess.run(
                ["sudo", "/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"],
                capture_output=True, text=True
            )
            return "Enabled" if "State = 1" in result.stdout else "Disabled"
        elif platform.system() == "Linux":  # Linux
            result = subprocess.run(
                ["ufw", "status"], capture_output=True, text=True
            )
            return "Enabled" if "active" in result.stdout.lower() else "Disabled"
        elif platform.system() == "Windows":  # Windows
            result = subprocess.run(
                ["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True
            )
            return "Enabled" if "State ON" in result.stdout else "Disabled"
        else:
            return "Unknown"
    except Exception as e:
        print(f"Firewall Check Error: {e}")
        return "Error"

# Function to check antivirus status (placeholder logic)
def check_antivirus_status():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["powershell", "-Command", "Get-MpComputerStatus | Select-Object -ExpandProperty AMServiceEnabled"],
                capture_output=True, text=True
            )
            return "Active" if "True" in result.stdout else "Inactive"
        # Basic placeholder for macOS/Linux
        return "No antivirus detected"
    except Exception as e:
        print(f"Antivirus Check Error: {e}")
        return "Error"

@app.route('/')
def index():
    # Run the speed test synchronously
    speed_results = run_speed_test()

    # Get system information
    operating_system = f"{platform.system()} {platform.version()}"
    password_strength = "Ensure you are using a strong password"  # Placeholder
    firewall_status = check_firewall_status()
    antivirus_status = check_antivirus_status()
    software_updates = "Up-to-date" if platform.system() == "Darwin" else "Check for updates manually"
    two_factor_authentication = "Check manual configuration for 2FA"  # Placeholder

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
