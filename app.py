from flask import Flask, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    # Initialize the speedtest-cli
    st = speedtest.Speedtest()
    st.get_best_server()
    
    # Perform the speed test
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6      # Convert to Mbps
    ping = st.results.ping  # Ping in ms

    return render_template('index.html', 
                           download_speed=download_speed, 
                           upload_speed=upload_speed, 
                           ping=ping)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
