from flask import Flask, render_template, request, jsonify
import speedtest
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_checks", methods=["POST"])
def run_checks():
    # Simulating system checks
    os_info = os.uname()
    password_strength = "Ensure you are using a strong password (not checked here)."
    firewall = "Disabled. Enable it for better security."
    software_updates = check_software_updates()
    antivirus = "No antivirus detected. Consider installing one for better security."
    two_factor_auth = "Check manual configuration for 2FA (not implemented yet)."

    # Speed test part
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1e6  # Mbps
        upload_speed = st.upload() / 1e6  # Mbps
        ping = st.results.ping
    except Exception as e:
        download_speed = upload_speed = ping = None
        print(f"Error running speedtest: {e}")

    # Return results to render on the page
    return render_template("index.html",
                           os=os_info,
                           password_strength=password_strength,
                           firewall=firewall,
                           software_updates=software_updates,
                           antivirus=antivirus,
                           two_factor_auth=two_factor_auth,
                           download_speed=download_speed,
                           upload_speed=upload_speed,
                           ping=ping)

def check_software_updates():
    try:
        result = subprocess.run(['softwareupdate', '-l'], capture_output=True, text=True)
        if "No new software available" in result.stdout:
            return "Your system is up-to-date."
        else:
            return "Updates available. Run 'softwareupdate -i -a' to install."
    except Exception as e:
        return f"Error checking for updates: {e}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
