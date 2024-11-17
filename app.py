from flask import Flask, render_template, request, jsonify
import os
import psutil
import speedtest

app = Flask(__name__)

@app.route("/")
def index():
    # Initial system check data
    os_info = os.uname()
    password_strength = "Ensure you're using a strong password"
    firewall = "Enabled"  # Mocked data, would need to check real firewall settings
    software_updates = "Up to date"  # Mocked data
    antivirus = "No antivirus detected"  # Mocked data
    two_factor_auth = "Enabled"  # Mocked data

    # System resource check using psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    # Internet speed test using speedtest-cli
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert from bits/sec to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits/sec to Mbps
    ping = st.results.ping

    return render_template("index.html",
        os=os_info,
        password_strength=password_strength,
        firewall=firewall,
        software_updates=software_updates,
        antivirus=antivirus,
        two_factor_auth=two_factor_auth,
        download_speed=download_speed,
        upload_speed=upload_speed,
        ping=ping,
        cpu_usage=cpu_usage,
        memory_info=memory_info.percent,
        disk_usage=disk_usage.percent
    )

@app.route("/run_checks", methods=["POST"])
def run_checks():
    return index()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
