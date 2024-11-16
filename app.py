from flask import Flask, render_template, request, jsonify
import platform
import speedtest
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # System Security Check Mock Data
    security_data = {
        "Operating System": platform.platform(),
        "Password Strength": "Ensure you are using a strong password (not checked here).",
        "Firewall": "Disabled. Enable it for better security.",
        "Software Updates": "Updates available. Run 'softwareupdate -i -a' to install.",
        "Antivirus": "No antivirus detected. Consider installing one for better security.",
        "2FA": "Check manual configuration for 2FA (not implemented yet)."
    }

    # Real-Time Internet Speed Test
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        speed_data = {
            "Download Speed": f"{download_speed:.2f} Mbps",
            "Upload Speed": f"{upload_speed:.2f} Mbps",
            "Ping": f"{ping:.2f} ms"
        }
    except Exception as e:
        speed_data = {
            "Error": "Unable to perform speed test. Please try again later."
        }

    return render_template('results.html', security=security_data, speed=speed_data)

@app.route('/download_results', methods=['GET'])
def download_results():
    results = {
        "System Security": {
            "Operating System": platform.platform(),
            "Password Strength": "Ensure you are using a strong password (not checked here).",
            "Firewall": "Disabled. Enable it for better security.",
            "Software Updates": "Updates available. Run 'softwareupdate -i -a' to install.",
            "Antivirus": "No antivirus detected. Consider installing one for better security.",
            "2FA": "Check manual configuration for 2FA (not implemented yet)."
        },
        "Internet Speed": {
            "Download Speed": f"{random.uniform(50, 200):.2f} Mbps",
            "Upload Speed": f"{random.uniform(10, 50):.2f} Mbps",
            "Ping": f"{random.uniform(10, 50):.2f} ms"
        }
    }

    # Return results as a JSON file
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

