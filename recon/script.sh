#!/bin/bash

set -e


HTTPX_URL="https://github.com/projectdiscovery/httpx/releases/download/v1.7.0/httpx_1.7.0_linux_amd64.zip"
CHAOS_URL="https://github.com/projectdiscovery/chaos-client/releases/download/v0.5.2/chaos-client_0.5.2_linux_amd64.zip"
KATANA_URL="https://github.com/projectdiscovery/katana/releases/download/v1.1.3/katana_1.1.3_linux_amd64.zip"


cd /tmp

echo "Downloading httpx..."
wget -q "$HTTPX_URL" -O httpx.zip
echo "Downloading chaos-client..."
wget -q "$CHAOS_URL" -O chaos-client.zip
echo "Downloading katana..."
wget -q "$KATANA_URL" -O katana.zip


unzip -o httpx.zip
unzip -o chaos-client.zip
unzip -o katana.zip


echo "Moving httpx to /usr/bin..."
sudo mv -f httpx /usr/bin/
echo "Moving chaos-client to /usr/bin..."
sudo mv -f chaos-client /usr/bin/
echo "Moving katana to /usr/bin..."
sudo mv -f katana /usr/bin/

echo "All tools installed to /usr/bin."
