from flask import Flask, render_template
import speedtest

app = Flask(__name__)

# Function to run the speed test
def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()  # Choose the best server based on ping
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    ping = st.results.ping  # Get the ping
    return download_speed, upload_speed, ping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # Run speed test and other checks
    download_speed, upload_speed, ping = run_speedtest()
    
    # Placeholder data for system checks (this should be replaced with actual checks)
    os_info = {
        "sysname": "macOS",  # Example data, replace with actual system info
        "machine": "arm64",
        "release": "15.1"
    }
    password_strength = "Ensure you are using a strong password."
    firewall = "Disabled. Enable it for better security."
    software_updates = "Updates available. Run 'softwareupdate -i -a' to install."
    antivirus = "No antivirus detected. Consider installing one for better security."
    two_factor_auth = "Check manual configuration for 2FA (not implemented yet)."
    
    # Return the results to the template
    return render_template('index.html', 
                           os=os_info,
                           password_strength=password_strength,
                           firewall=firewall,
                           software_updates=software_updates,
                           antivirus=antivirus,
                           two_factor_auth=two_factor_auth,
                           download_speed=download_speed, 
                           upload_speed=upload_speed, 
                           ping=ping)

if __name__ == '__main__':
    app.run(debug=True)
