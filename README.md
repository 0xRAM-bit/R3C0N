# R3C0N

⚙️ Setup Instructions
1️⃣ Clone the Repository

git clone https://github.com/0xRAM-bit/R3C0N.git
cd R3C0N

2️⃣ Run the Setup Script

The setup script will:

    Download and install httpx, katana, chaos-client

    Create a Python virtual environment

    Install Python requirements automatically

chmod +x setup.sh
./setup.sh

3️⃣ Activate the Virtual Environment

Activate the environment before running the tool:

source venv/bin/activate

🚀 Usage
Run the main tool:

python3 main.py

Example commands:

python3 main.py portscan -t target.com
python3 main.py dir -u https://target.com/FUZZ -w wordlist.txt
python3 main.py find_payload -p xss -t filter_bypass

🔄 Update Instructions

If you want the latest updates:

git pull
source venv/bin/activate
pip install -r requirements.txt

Or optionally, you can implement an --update flag later to automate this.
💡 Features

    Port scanning (nmap wrapper)

    Directory brute-forcing (ffuf wrapper)

    Subdomain enumeration (using chaos-client)

    Crawling (katana wrapper)

    Parameter finder for vulnerability classes

    Payload finder (XSS, SQLi, SSTI, etc.)

📥 Requirements

    Linux (Tested on Kali, Parrot, Ubuntu)

    Python 3.x

    httpx, katana, chaos-client (installed via setup.sh)

🤝 Contributing

PRs and suggestions are welcome. Open an issue or fork the repo to contribute.
⚠️ Legal Disclaimer

This tool is for educational and authorized security testing only. Misuse may lead to legal consequences.
👨‍💻 Author

    0xRAM-bit
