PortSwigger Race Condition Lab - Multi-Endpoint Exploit
https://portswigger.net/content/images/logos/burger-2021.svg
https://img.shields.io/badge/Python-3.8%252B-blue.svg
https://img.shields.io/badge/License-MIT-green.svg

A Python-based exploit to solve the PortSwigger Web Security Academy's "Race conditions: multi-endpoint" lab. This script demonstrates how to exploit race condition vulnerabilities across multiple endpoints simultaneously.

📋 Lab Overview
Lab Title: Race conditions: multi-endpoint
Difficulty: Practitioner
Category: Race Conditions
Lab Link: PortSwigger Lab

Lab Description
This lab contains a race condition vulnerability in its purchasing workflow. To solve the lab, you need to exploit this vulnerability across multiple endpoints to purchase a jacket at an discounted price.

🚀 Prerequisites
Python 3.8 or higher

requests library

beautifulsoup4 library (for HTML parsing)

Access to the PortSwigger lab environment

Basic understanding of race condition vulnerabilities

📦 Installation
Clone this repository:

bash
git clone https://github.com/your-username/portswigger-race-condition-exploit.git
cd portswigger-race-condition-exploit
Install required dependencies:

bash
pip install requests beautifulsoup4
🔧 Configuration
Before running the script, you need to configure it with your lab-specific details:

Get your lab URL:

Access the lab from your PortSwigger account

Copy the unique lab URL (e.g., https://abc123.web-security-academy.net)

Get your session cookie:

Login to the lab in your browser

Open Developer Tools (F12)

Go to Application/Storage tab → Cookies

Copy the value of the session cookie

Update the script:

Open race_condition_exploit.py

Replace the placeholder values:

python
LAB_URL = "https://your-lab-id.web-security-academy.net"
SESSION_COOKIE = "your-actual-session-cookie"
🎯 Usage
Basic Execution
bash
python race_condition_exploit.py
Advanced Options
bash
# Run with increased thread count
python race_condition_exploit.py --threads 20

# Run with specific endpoints
python race_condition_exploit.py --endpoint-add /cart --endpoint-checkout /checkout
Command Line Arguments
Argument	Description	Default
--threads	Number of concurrent threads	15
--attempts	Attempts per thread	10
--delay	Delay between requests (ms)	10
--verbose	Enable verbose output	False
🧠 How It Works
Vulnerability Analysis
The lab contains a race condition in the purchase workflow where:

Items are added to cart

Discounts are applied

Checkout process completes

By sending requests to these endpoints simultaneously, we can exploit timing windows where business logic validation occurs inconsistently.

Exploit Strategy
CSRF Token Extraction: Automatically retrieves the CSRF token from the cart page

Concurrent Request Flood: Uses Python threading to send simultaneous requests to multiple endpoints

Race Condition Trigger: Creates timing conflicts between:

Adding items to cart (/cart)

Applying discounts (/cart/discount)

Completing checkout (/cart/checkout)

Verification: Checks if the purchase was successful

Key Components
Thread Management: Creates multiple threads for each endpoint

Session Persistence: Maintains the same session across all requests

Error Handling: Gracefully handles network errors and timeouts

Result Verification: Automatically checks if the exploit was successful

📝 Code Structure
text
race_condition_exploit.py
├── RaceConditionExploit (Class)
│   ├── __init__() - Initialize with lab details
│   ├── get_csrf_token() - Extract CSRF token from HTML
│   ├── discover_endpoints() - Find relevant endpoints
│   ├── race_attack() - Main exploit method
│   └── verify_exploit() - Check if lab was solved
├── attack_endpoint() - Thread function for requests
└── main() - Command line interface and execution
🛠️ Customization
Modifying Endpoints
If the lab uses different endpoints, update the endpoints list:

python
endpoints = [
    ("/cart", {"productId": "1", "quantity": "1"}, "Add to Cart"),
    ("/api/checkout", {"csrf": self.csrf_token}, "Checkout"),
    ("/apply-discount", {"code": "SIGNUP30"}, "Discount")
]
Adjusting Timing
Modify the delay between requests for different network conditions:

python
# Increase delay for slower networks
time.sleep(0.05)  # 50ms delay
🧪 Testing
Verification Steps
After running the script:

Check if "Lab solved" message appears

Visit the cart page to confirm purchase

Verify the jacket was purchased at discounted price

Troubleshooting
Session expired: Renew your session cookie

CSRF token issues: The script auto-extracts tokens, but verify the token field name

Network errors: Check your internet connection and lab accessibility

Thread limitations: Adjust thread count based on your system capabilities

🔒 Ethical Considerations
This exploit script is designed for:

Educational purposes only

PortSwigger Web Security Academy labs

Legal penetration testing environments

Do not use this script against systems without explicit permission.

📚 Learning Objectives
By studying this exploit, you'll understand:

Race condition vulnerabilities in web applications

Multi-endpoint race condition exploitation

Concurrent programming in security testing

Session management in automated exploits

CSRF token handling in authenticated requests

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
PortSwigger for providing excellent web security training materials

The cybersecurity community for continuous research and knowledge sharing

⚠️ Disclaimer
This tool is provided for educational purposes only. The authors are not responsible for any misuse or damage caused by this program. Always obtain proper authorization before testing any systems.

