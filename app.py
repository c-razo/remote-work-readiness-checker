from flask import Flask, render_template, jsonify, request
import speedtest
import os

app = Flask(__name__)

@app.route('/')
def index():
    tools = "Here are the tools you can use for remote work!"  # You can dynamically generate this data
    return render_template('index.html', tools=tools)

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # Perform system checks and speed test here
    st = speedtest.Speedtest()
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
