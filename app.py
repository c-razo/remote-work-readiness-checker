from flask import Flask, render_template, request, redirect, url_for
from features.security_check import system_security_check
from features.speed_test import internet_speed_test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_checks', methods=['POST'])
def run_checks():
    # Run system security check
    security_results = system_security_check()

    # Run internet speed test
    speed_results = internet_speed_test()

    return render_template('results.html', security=security_results, speed=speed_results)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

