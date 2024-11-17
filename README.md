# Remote Work Readiness Checker

## Overview
The **Remote Work Readiness Checker** is a Python-based tool designed to help individuals optimize their remote work setup. This tool evaluates key aspects of a user's environment, including security, internet speed, and productivity tools. By using this checker, remote workers can ensure they have a secure and efficient working setup, which is essential for maintaining productivity and safeguarding sensitive information.

## Key Features
- **Security Assessment**: Checks if critical security features are enabled on the system, such as firewall status, antivirus software, and the latest software updates.
- **Internet Speed Evaluation**: Measures your internet connection’s upload, download speeds, and latency to ensure you have an optimal connection for remote work.
- **Productivity Tools Configuration**: Verifies the setup of essential productivity tools, ensuring they are configured for maximum efficiency.

## Installation

To get started, you’ll need to install the required dependencies. Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/c-razo/remote-work-readiness-checker.git
   ```

2. **Navigate into the project directory:**
   ```bash
   cd remote-work-readiness-checker
   ```

3. **Install the necessary Python dependencies:**
   You can install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure you have the necessary system tools:**
   - The security assessment tool may require administrator privileges to check firewall settings.
   - The internet speed test may require access to your network interfaces, so ensure that the tool can access the necessary system resources.

## Usage

Once the setup is complete, you can run the tool by executing the main Python script. This will trigger the checks and generate a report.

To run the tool:
1. **Execute the script:**
   ```bash
   python app.py
   ```

2. **Follow the on-screen instructions** to start the assessment.

3. **Review the results** in the terminal or on the generated HTML report, depending on your configuration.

### Example Output:
- **Security**: The tool will display whether your firewall and antivirus software are active, and if any software updates are pending.
- **Internet Speed**: You'll see the measured download/upload speeds and latency, with recommendations if the speeds are below a recommended threshold.
- **Productivity Tools**: If configured, it will list the status of commonly used tools (e.g., VPNs, email clients, etc.) and provide suggestions for improvements.

## Screenshots

### 1. Welcome Page
This is the initial landing page of the app, where users can click "Run Checks" to begin the evaluation.

![Welcome Page](./screenshot_1.png)  
*Figure 1: Welcome page of the Remote Work Readiness Checker.*

### 2. Results Overview
Once the checks are completed, users will see a summary of the results, including their operating system info, password strength, firewall status, software updates, and more.

![Results Page](./screenshot_2.png)  
*Figure 2: The results summary after running the checks.*

### 3. Detailed Results
This screenshot shows the detailed results, including specific recommendations such as enabling a firewall, updating software, and installing antivirus software.

![Detailed Results](./screenshot_3.png)  
*Figure 3: Detailed breakdown of system and internet performance checks.*

### 4. Running the App on Localhost
The server can be accessed locally at `http://127.0.0.1:5000/` and the remote device at `http://10.0.0.86:5001/`.

![Flask Server Running](./screenshot_4.png)  
*Figure 4: Flask server running on localhost and remote address.*

### 5. Running Internet Speed Tests
After pressing "Run Checks," the internet speed tests are displayed, showcasing the download and upload speeds, as well as ping.

![Speed Test Results](./screenshot_5.png)  
*Figure 5: Internet speed test results including download/upload speed and ping.*

### 6. Checking Error for Port 5000
In case of the "Port 5000 is in use" error, ensure that the AirPlay Receiver service is turned off. Below, the error message and a solution are displayed.

![Error Message](./screenshot_6.png)  
*Figure 6: Error message related to port 5000 being in use.*

### 7. Disabling AirPlay Receiver
Here’s how to turn off the AirPlay Receiver service, which may be occupying port 5000 and causing the "Port in Use" error.

![Disabling AirPlay](./screenshot_7.png)  
*Figure 7: Instructions to disable AirPlay Receiver on macOS.*

### Web Interface
The application displays results in a clean and structured interface, accessible via any browser.

## Business Use
Remote Work Readiness Checker is available for corporate licensing. This allows companies to use the tool internally across multiple users under a single license agreement.

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

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
- **Speedtest-cli**: Used for internet speed evaluation.
- **psutil**: Used for checking system information (e.g., firewall status, CPU usage).
