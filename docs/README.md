# Customizable Terminal-Based Social Media Dashboard

## Overview
This is a customizable terminal-based dashboard for managing multiple social media accounts (Twitter, Reddit, Mastodon) from a single terminal interface.

## Features
- View feeds from multiple social media platforms.
- Interact with posts (like, retweet, reply, comment).
- Support for multiple accounts.
- Customizable themes and layouts.

## Installation

### Prerequisites
- [Termux](https://termux.com/) installed on your device.
- Python 3.8+ installed.

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/social-media-dashboard.git
    ```
    ```bash
    cd social-media-dashboard
    ```

2. Run the setup script:
    ```bash
    bash scripts/setup.sh
    ```

3. Configure your API keys by editing `config/user_config.yaml`.

4. Run the application:
    ```bash
    python src/main.py
    ```

## Usage
Use the keyboard shortcuts to navigate through the feeds and interact with the posts. Customize the appearance and layout by editing the configuration files in `config/`.

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
