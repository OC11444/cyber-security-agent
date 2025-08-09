#!/bin/bash
# start_assistant.sh — Full Installer + Launcher for Cyber Assistant + ICP

echo "🔧 Cyber Assistant: Full Installer + ICP Canister Launcher"

# Step 1: Ask for sudo password early
echo "🔐 Requesting sudo to install system dependencies (only once)..."
sudo -v

# Step 2: Install system-level dependencies
echo "📦 Installing required system packages..."
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-venv python3-pyaudio libffi-dev libssl-dev

# Step 3: Ensure DFX is installed
if ! command -v dfx &> /dev/null; then
  echo "📦 Installing DFX (Internet Computer SDK)..."
  sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
  echo "✅ DFX installed. Please restart your terminal and rerun this script."
  exit 1
fi

# Step 4: Activate virtual environment
if [ ! -d "venv" ]; then
  echo "🐍 Creating virtual environment..."
  python3 -m venv venv
fi

echo "🧪 Activating virtual environment..."
source venv/bin/activate

# Step 5: Install Python dependencies
echo "📥 Installing Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 6: Start local ICP backend if dfx.json exists
if [ -f "dfx.json" ]; then
  echo "📡 Starting local ICP canister backend..."
  dfx start --background

  echo "🛠️  Deploying canisters..."
  dfx deploy

  echo "✅ Canisters deployed successfully!"
else
  echo "⚠️  No dfx.json found. Skipping canister launch."
fi

# Step 7: Choose assistant mode
echo ""
echo "🌐 Choose a mode to launch:"
echo "1. Live Mode"
echo "2. Demo Mode"
read -p "Enter your choice [1/2]: " choice

# Step 8: Launch assistant
if [ "$choice" == "1" ]; then
  echo "🚀 Launching in Live Mode..."
  python main.py --live
elif [ "$choice" == "2" ]; then
  echo "🧪 Launching in Demo Mode..."
  python main.py --demo
else
  echo "❌ Invalid option. Please choose 1 or 2."
  exit 1
fi
