from flask import Flask, render_template
import speedtest
import platform

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Get system information
        operating_system = f"{platform.system()} {platform.version()}"
        password_strength = "Ensure you are using a strong password"  # Placeholder
        firewall_status = "Disabled"  # Placeholder, replace with real logic
        software_updates = "Updates available"  # Placeholder
        antivirus_status = "No antivirus detected"  # Placeholder
        two_factor_authentication = "Check manual configuration for 2FA"  # Placeholder

        # Run speed test
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = round(st.download() / 1e6, 2)  # Convert to Mbps, round to 2 decimals
        upload_speed = round(st.upload() / 1e6, 2)  # Convert to Mbps, round to 2 decimals
        ping = st.results.ping

    except Exception as e:
        # Handle errors (e.g., no internet connection)
        operating_system = "Unknown"
        password_strength = "Error checking password strength"
        firewall_status = "Error"
        software_updates = "Error"
        antivirus_status = "Error"
        two_factor_authentication = "Error"
        download_speed = "Error"
        upload_speed = "Error"
        ping = "Error"
        print(f"Error: {e}")  # Log error for debugging

    # Render template with gathered data
    return render_template(
        'index.html',
        operating_system=operating_system,
        password_strength=password_strength,
        firewall_status=firewall_status,
        software_updates=software_updates,
        antivirus_status=antivirus_status,
        two_factor_authentication=two_factor_authentication,
        download_speed=download_speed,
        upload_speed=upload_speed,
        ping=ping
    )

if __name__ == '__main__':
    app.run(debug=True)
