# Installation Guide

## Prerequisites
Before you start, ensure you have the following installed:

1. **Termux**: Available from the Google Play Store or F-Droid.
2. **Python 3.8+**: This project requires Python 3.8 or higher.

## Step-by-Step Installation

### 1. Installing Termux and Python
Open Termux and update the package list:
  ```bash
  pkg update && pkg upgrade
  ```
Install Python:
  ```bash
  pkg install python
  ```
Verify the installation:
  ```bash
  python --version
  ```
### 2. Cloning the Repository
Clone this repository to your local environment:
  ```bash
  git clone https://github.com/yourusername/social-media-dashboard.git
  ```
  ```bash
  cd social-media-dashboard
  ```
### 3. Setting Up the Environment
Run the setup script to install dependencies and set up the configuration:
  ```bash
  bash scripts/setup.sh
  ```
### 4. Configuring API Keys
Before you can use the dashboard, you need to set up API keys for each social media platform. Open the config/user_config.yaml file and replace the placeholders with your API keys.

### 5. Running the Application
Finally, start the application:
  ```bash
  python src/main.py
  ```
Now you should see the terminal-based dashboard displaying your social media feeds.

### **6. `CONTRIBUTING.md`**
Guidelines for contributing to the project.

```markdown
# Contributing to the Social Media Dashboard

## How to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add new feature'`.
5. Push to the branch: `git push origin feature-branch-name`.
6. Submit a pull request.

## Code of Conduct
Please be respectful and considerate of others when contributing to this project. We expect all contributors to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

## Pull Request Guidelines
- Ensure your code follows the project's coding style.
- Write clear, concise commit messages.
- Include tests for any new functionality.
- Document your code, especially for new modules or features.

## Reporting Issues
If you find a bug or have a feature request, please create an issue on the GitHub repository.
