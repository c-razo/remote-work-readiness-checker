from flask import Flask, render_template, jsonify
import speedtest
import platform
import threading

app = Flask(__name__)

# Global variables to hold speed test results
speed_results = {
    "download_speed": None,
    "upload_speed": None,
    "ping": None
}

# Function to perform the speed test asynchronously
def run_speed_test():
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

@app.route('/')
def index():
    # Start speed test in a background thread
    threading.Thread(target=run_speed_test).start()

    # Get system information
    operating_system = f"{platform.system()} {platform.version()}"
    password_strength = "Ensure you are using a strong password"  # Placeholder
    firewall_status = "Enabled" if platform.system() == "Linux" else "Check manually"
    antivirus_status = "Active" if platform.system() == "Windows" else "No antivirus detected"
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
    return jsonify(speed_results)

if __name__ == '__main__':
    app.run(debug=True)
