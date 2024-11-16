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

## Installation

### Prerequisites
- Python 3.6 or higher
- [speedtest-cli](https://pypi.org/project/speedtest-cli/) library for internet speed testing

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/c-razo/remote-work-readiness-checker.git
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

2. Run the main script to check system readiness:
   ```bash
   python main.py
   ```

## Example Output
```plaintext
Running System Security Check...
Operating System: Darwin (Version: ... )
Password Strength: Ensure you are using a strong password (not checked here).
Firewall: Disabled. Enable it for better security.
Software Updates: Up to date
Antivirus: No antivirus detected. Consider installing one for better security.
2FA: Check manual configuration for 2FA (not implemented yet).

Running Internet Speed Test...
Download Speed: 185.25 Mbps
Upload Speed: 24.46 Mbps
Ping: 26.23 ms
```

## Latest Milestone Update
The Remote Work Readiness Checker is now accessible from any device on the local network, including mobile devices, thanks to improved host binding (`0.0.0.0`). Additionally:
- The firewall blocking issue on macOS has been resolved.
- Features like system security checks and internet speed tests are fully operational.

## Business Use

Remote Work Readiness Checker is available for corporate licensing. This allows companies to use the tool internally across multiple users under a single license agreement.

### Contact
For inquiries and licensing fees, please contact [christopher.razo@icloud.com].

## Recommended Tools for Remote Work

To enhance your remote work environment, we recommend the following tools:

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
```

