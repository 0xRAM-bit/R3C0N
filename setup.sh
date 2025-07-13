#!/bin/bash

set -e

echo "[*] Uploading trojan to your PC... [OK]"
sleep 1
echo "[*] Sending your browsing history to my C2 server... [OK]"
sleep 1
echo "[*] Cracking your router password... please wait..."
sleep 1
echo "[*] Connected to your fridge. Temperature: 4°C [OK]"
sleep 1
echo "[*] Proceeding with actual installation... (just kidding so far)"


HTTPX_URL="https://github.com/projectdiscovery/httpx/releases/download/v1.7.0/httpx_1.7.0_linux_amd64.zip"
CHAOS_URL="https://github.com/projectdiscovery/chaos-client/releases/download/v0.5.2/chaos-client_0.5.2_linux_amd64.zip"
KATANA_URL="https://github.com/projectdiscovery/katana/releases/download/v1.1.3/katana_1.1.3_linux_amd64.zip"

cd /tmp

echo "[*] Downloading illegal hacking tools... just kidding, downloading legit security tools:"
echo "[+] Downloading httpx..."
wget -q "$HTTPX_URL" -O httpx.zip
echo "[+] Downloading chaos-client..."
wget -q "$CHAOS_URL" -O chaos-client.zip
echo "[+] Downloading katana..."
wget -q "$KATANA_URL" -O katana.zip


unzip -o httpx.zip
unzip -o chaos-client.zip
unzip -o katana.zip


echo "[*] Installing backdoors... oops, meant 'security tools' into /usr/bin/..."
sudo mv -f httpx /usr/bin/
sudo mv -f chaos-client /usr/bin/
sudo mv -f katana /usr/bin/
echo "[+] All tools successfully planted... I mean installed."


echo "[*] Establishing persistence... (setting up Python virtual environment)"
python3 -m venv venv
source venv/bin/activate

echo "[*] Deploying additional payloads... (installing Python dependencies)"
pip install -r requirements.txt

echo "[*] Cleanup traces... done."
echo "[✔] Setup completed."
echo "[*] To activate the venv later: source venv/bin/activate"
echo "[*] Remember: Your fridge is still connected."
