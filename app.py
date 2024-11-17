from flask import Flask, render_template, request, flash, send_file
import speedtest
import os
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session-based flash messages

# Route to the index page where the form is displayed
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tools = request.form.get('tools')

        if not tools:  # Check if the tools field is empty
            flash("Please enter your remote work tools.", 'error')
        else:
            return render_template('index.html', tools=tools)

    return render_template('index.html')

# Route to run the checks
@app.route('/run_checks', methods=['POST'])
def run_checks():
    # System info
    os_info = os.uname()

    # Internet Speed Test
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # convert from bits to Mbps
    upload_speed = st.upload() / 1_000_000  # convert from bits to Mbps
    ping = st.results.ping

    # Placeholder values for system security
    password_strength = "Ensure you are using a strong password (not checked here)."
    firewall = "Disabled. Enable it for better security."
    software_updates = "Updates available. Run 'softwareupdate -i -a' to install."
    antivirus = "No antivirus detected. Consider installing one for better security."
    two_factor_auth = "Check manual configuration for 2FA (not implemented yet)."

    # Generate results as text
    results = f"""
    System Security Check:
    Operating System: {os_info.sysname} {os_info.machine} ({os_info.release})
    Password Strength: {password_strength}
    Firewall: {firewall}
    Software Updates: {software_updates}
    Antivirus: {antivirus}
    2FA: {two_factor_auth}
    
    Internet Speed Test:
    Download Speed: {download_speed:.2f} Mbps
    Upload Speed: {upload_speed:.2f} Mbps
    Ping: {ping} ms
    """

    # Save the results to a file
    results_file = io.StringIO()
    results_file.write(results)
    results_file.seek(0)
    return send_file(results_file, as_attachment=True, download_name="remote_work_readiness_results.txt", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
