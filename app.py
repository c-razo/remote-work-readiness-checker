from flask import Flask, render_template
import speedtest
import platform

app = Flask(__name__)

@app.route('/')
def index():
    # Get system information
    operating_system = platform.system() + " " + platform.version()
    password_strength = "Ensure you are using a strong password"
    firewall_status = "Disabled"  # You can replace this with real logic
    software_updates = "Updates available"  # Replace with actual logic
    antivirus_status = "No antivirus detected"
    two_factor_authentication = "Check manual configuration for 2FA"

    # Run speed test
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e6  # Convert to Mbps
    upload_speed = st.upload() / 1e6  # Convert to Mbps
    ping = st.results.ping

    return render_template('index.html', 
                           operating_system=operating_system, 
                           password_strength=password_strength,
                           firewall_status=firewall_status,
                           software_updates=software_updates,
                           antivirus_status=antivirus_status,
                           two_factor_authentication=two_factor_authentication,
                           download_speed=download_speed,
                           upload_speed=upload_speed,
                           ping=ping)

if __name__ == '__main__':
    app.run(debug=True)
