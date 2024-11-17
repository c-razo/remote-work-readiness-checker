# Remote Work Readiness Checker

## Overview
The Remote Work Readiness Checker is a Python-based tool designed to evaluate remote work environments. It provides insights into system security, internet speed, and configuration of essential tools, helping users optimize their setup for productivity and security.

## Features
- **System Security Check**:
  - Checks operating system details.
  - Flags default usernames.
  - Recommends strong passwords.
  - Checks firewall status (macOS only).
  - Checks for software updates (macOS only).
  - Recommends antivirus software.
  - Highlights the importance of Two-Factor Authentication (2FA).

- **Internet Speed Test**:
  - Measures download speed, upload speed, and ping time, providing valuable metrics for remote work performance.

- **Interactive Web Interface**:
  - User-friendly web interface powered by Flask.
  - Displays results in a structured and easy-to-read format.

## Installation

### Prerequisites
- Python 3.6 or higher
- [speedtest-cli](https://pypi.org/project/speedtest-cli/) library for internet speed testing

### Steps
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/remote-work-readiness-checker.git
    cd remote-work-readiness-checker
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the virtual environment is activated:
    ```bash
    source venv/bin/activate
    ```

2. Run the Flask app:
    ```bash
    python app.py --host=0.0.0.0 --port=5001
    ```

3. Access the application in your browser:
    ```bash
    http://<your-ip-address>:5001
    ```

## Example Output
### System Security Check
```text
Running System Security Check...
Operating System: macOS 15.1 - arm64
Password Strength: Ensure you are using a strong password (not checked here).
Firewall: Disabled. Enable it for better security.
Software Updates: Updates available. Run 'softwareupdate -i -a' to install.
Antivirus: No antivirus detected. Consider installing one for better security.
2FA: Check manual configuration for 2FA (not implemented yet).
```

### Internet Speed Test
```text
Running Internet Speed Test...
Download Speed: 185.25 Mbps
Upload Speed: 24.46 Mbps
Ping: 26.23 ms
```

### Web Interface
The application displays results in a clean and structured interface, accessible via any browser.

## Business Use
Remote Work Readiness Checker is available for corporate licensing. This allows companies to use the tool internally across multiple users under a single license agreement.

### Contact
For inquiries and licensing fees, please contact [christopher.razo@icloud.com].

## Recommended Tools for Remote Work

### VPN Services
- [NordVPN](YOUR_AFFILIATE_LINK) – High-speed servers with strong privacy features.
- [ExpressVPN](YOUR_AFFILIATE_LINK) – Excellent performance and strong encryption.
- [Surfshark VPN](YOUR_AFFILIATE_LINK) – Affordable and user-friendly.

### Antivirus Software
- [McAfee Antivirus](YOUR_AFFILIATE_LINK) – Comprehensive protection with web protection.
- [Norton Antivirus](YOUR_AFFILIATE_LINK) – Reliable malware protection with identity monitoring.
- [Bitdefender](YOUR_AFFILIATE_LINK) – Robust security with minimal system impact.

### Internet Speed Optimization
- [Google Nest WiFi](YOUR_AFFILIATE_LINK) – Reliable mesh Wi-Fi system.
- [Netgear Orbi](YOUR_AFFILIATE_LINK) – High-speed and excellent coverage.

### Remote Work Productivity
- [Grammarly](YOUR_AFFILIATE_LINK) – Improve grammar and clarity in communication.
- [LastPass](YOUR_AFFILIATE_LINK) – Manage passwords securely.
- [Microsoft 365](YOUR_AFFILIATE_LINK) – Essential productivity tools for remote work.

## Contributing
Contributions are welcome! Please submit a pull request or file an issue if you’d like to help.

## License
- **Individual Use**: Licensed under the [MIT License](LICENSE.md).
- **Business Use**: For corporate licensing, refer to the [Corporate License Agreement](LICENSE_CORPORATE.md).

## Notes
- If you encounter the error "Port 5000 is in use," it may be because the AirPlay Receiver service is active on macOS. You can resolve this issue by turning off the AirPlay Receiver:
  - Go to **System Preferences** → **General** → **AirDrop & Handoff**, and disable the AirPlay Receiver service.

## Screenshots

### 1. Welcome Page
This is the initial landing page of the app, where users can click "Run Checks" to begin the evaluation.

![Welcome Page](./screenshots/screenshot_1.png)  
*Figure 1: Welcome page of the Remote Work Readiness Checker.*

### 2. Results Overview
Once the checks are completed, users will see a summary of the results, including their operating system info, password strength, firewall status, software updates, and more.

![Results Page](./screenshots/screenshot_2.png)  
*Figure 2: The results summary after running the checks.*

### 3. Detailed Results
This screenshot shows the detailed results, including specific recommendations such as enabling a firewall, updating software, and installing antivirus software.

![Detailed Results](./screenshots/screenshot_3.png)  
*Figure 3: Detailed breakdown of system and internet performance checks.*

### 4. Running the App on Localhost
The server can be accessed locally at `http://127.0.0.1:5000/` and the remote device at `http://10.0.0.86:5001/`.

![Flask Server Running](./screenshots/screenshot_4.png)  
*Figure 4: Flask server running on localhost and remote address.*

### 5. Running Internet Speed Tests
After pressing "Run Checks," the internet speed tests are displayed, showcasing the download and upload speeds, as well as ping.

![Speed Test Results](./screenshots/screenshot_5.png)  
*Figure 5: Internet speed test results including download/upload speed and ping.*

### 6. Checking Error for Port 5000
In case of the "Port 5000 is in use" error, ensure that the AirPlay Receiver service is turned off. Below, the error message and a solution are displayed.

![Error Message](./screenshots/screenshot_6.png)  
*Figure 6: Error message related to port 5000 being in use.*

### 7. Disabling AirPlay Receiver
Here’s how to turn off the AirPlay Receiver service, which may be occupying port 5000 and causing the "Port in Use" error.

![Disabling AirPlay](./screenshots/screenshot_7.png)  
*Figure 7: Instructions to disable AirPlay Receiver on macOS.*
