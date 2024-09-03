#!/bin/bash

echo "Setting up the environment..."

# Install Python dependencies
pip install -r requirements.txt

# Copy default config to user config if it doesn't exist
if [ ! -f config/user_config.yaml ]; then
    cp config/default_config.yaml config/user_config.yaml
fi

echo "Setup complete."
