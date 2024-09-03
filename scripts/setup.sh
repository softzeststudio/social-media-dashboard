#!/bin/bash

echo "Setting up the environment..."

# Update and install dependencies
pkg update && pkg upgrade -y
pkg install -y python clang make cmake libffi openssl

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install Python dependencies
pip install -r requirements.txt

echo "Setup complete."
