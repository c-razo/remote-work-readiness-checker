from flask import Flask, render_template, request, jsonify
import speedtest
import platform
import re

app = Flask(__name__)

# Function to perform the speed test
def run_speed_test():
    speed_results = {}
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        speed_results["download_speed"] = round(st.download() / 1e6, 2)  # Mbps
        speed_results["upload_speed"] = round(st.upload() / 1e6, 2)  # Mbps
        speed_results["ping"] = round(st.results.ping, 2)
    except Exception as e:
        # Fallback values for errors
        speed_results["download_speed"] = "Unavailable"
        speed_results["upload_speed"] = "Unavailable"
        speed_results["ping"] = "Unavailable"
        print(f"Speedtest Error: {e}")
    return speed_results

# Function to check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Weak: Include uppercase and lowercase letters"
    if not re.search("[0-9]", password):
        return "Weak: Include at least one number"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Include special characters"
    return "Strong"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Run the spee
