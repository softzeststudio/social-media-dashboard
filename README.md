<!-- Project Title -->
<h1 align="center">📊 Customizable Terminal-Based Social Media Dashboard</h1>

<p align="center">
  <b>Manage multiple social media accounts from a single terminal-based dashboard.</b>
  <br>
  <img src="https://img.shields.io/github/stars/yourusername/social-media-dashboard?style=flat-square">
  <img src="https://img.shields.io/github/forks/yourusername/social-media-dashboard?style=flat-square">
  <img src="https://img.shields.io/github/issues/yourusername/social-media-dashboard?style=flat-square">
  <img src="https://img.shields.io/github/license/yourusername/social-media-dashboard?style=flat-square">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

<!-- Introduction -->
## 🚀 Introduction

The **Customizable Terminal-Based Social Media Dashboard** is a powerful and flexible tool that allows you to manage multiple social media platforms like Twitter, Reddit, and Mastodon directly from your terminal. It is designed to be lightweight, easy to configure, and extensible.

---

<!-- Features -->
## ✨ Features

- **Multi-Platform Support**: Manage Twitter, Reddit, and Mastodon accounts.
- **Customizable Interface**: Change themes, layouts, and configure your dashboard to suit your preferences.
- **Secure and Private**: Your API keys and credentials are securely stored and never shared.
- **Lightweight**: Runs smoothly on low-resource environments, perfect for Termux users.
- **Extendable**: Easily add new social media platforms or customize functionality.

---

<!-- Installation -->
## 🛠️ Installation

### Prerequisites

- Termux installed on your Android device.
- Python 3.8+ installed.

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/social-media-dashboard.git
    cd social-media-dashboard
    ```

2. **Run the setup script**:
    ```bash
    bash scripts/setup.sh
    ```

3. **Configure API keys**:
    - Update `config/user_config.yaml` with your API keys for Twitter, Reddit, and Mastodon.

4. **Run the application**:
    ```bash
    python src/main.py
    ```

---

<!-- Usage -->
## 📈 Usage

After running the application, you'll see a terminal-based dashboard displaying feeds from your connected social media accounts. Use keyboard shortcuts to navigate through the feeds and interact with posts.

### Keyboard Shortcuts

- **`j`** / **`k`**: Scroll down/up.
- **`Enter`**: View post details.
- **`l`**: Like/Upvote a post.
- **`r`**: Retweet/Comment on a post.
- **`q`**: Quit the dashboard.

---

<!-- Screenshots -->
## 🖼️ Screenshots

<p align="center">
  <img src="https://via.placeholder.com/600x400?text=Dashboard+Screenshot+1" alt="Screenshot 1">
  <img src="https://via.placeholder.com/600x400?text=Dashboard+Screenshot+2" alt="Screenshot 2">
</p>

---

<!-- Contributing -->
## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

---

<!-- License -->
## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<!-- Footer -->
<p align="center">
  Made with ❤️ by <a href="https://github.com/softzeststudio">SoftZest Studio</a>
</p>
