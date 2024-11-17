from flask import Flask, render_template, jsonify, request
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    # Here we define a placeholder message for remote work tools
    tools = "Here are the tools you can use for remote work!"  # Replace with actual tools data
    return render_template('index.html', tools=tools)

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # Perform system checks and speed test here
    st = speedtest.Speedtest()
    
    # Run the speed test for download, upload, and ping
    download_speed = st.download() / 10**6  # Convert from bits to megabits
    upload_speed = st.upload() / 10**6  # Convert from bits to megabits
    ping = st.results.ping

    # Return the results as JSON
    return jsonify({
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'ping': ping
    })

if __name__ == '__main__':
    app.run(debug=True)
