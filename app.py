from flask import Flask, render_template, jsonify, request
import speedtest
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # Perform system checks and speed test here
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert from bits to megabits
    upload_speed = st.upload() / 10**6  # Convert from bits to megabits
    ping = st.results.ping
    
    # For simplicity, using placeholders for system security details:
    os_info = os.uname()
    password_strength = "Strong (example)"
    firewall = "Enabled"
    software_updates = "Up to date"
    antivirus = "No antivirus detected"
    two_factor_auth = "Not configured"

    # Return the results as JSON
    return render_template('index.html', 
                           tools=request.form.get('tools'),
                           download_speed=download_speed,
                           upload_speed=upload_speed,
                           ping=ping,
                           os=os_info,
                           password_strength=password_strength,
                           firewall=firewall,
                           software_updates=software_updates,
                           antivirus=antivirus,
                           two_factor_auth=two_factor_auth)

if __name__ == '__main__':
    app.run(debug=True)
