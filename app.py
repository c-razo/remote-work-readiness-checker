from flask import Flask, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    # Perform system checks and speed test here (if necessary)
    tools = "Here are the tools you can use for remote work!"  # Replace with actual tools data

    # This is where you collect or generate the tools data.
    # You can replace the string with dynamic data or other logic if you have real tools data.
    
    return render_template('index.html', tools=tools)

if __name__ == '__main__':
    app.run(debug=True)
