# src/main.py

from core.dashboard import SocialMediaDashboard
from core.config_manager import ConfigManager

def main():
    # Load user configuration
    config = ConfigManager.load_config()

    # Initialize the social media dashboard
    dashboard = SocialMediaDashboard(config)
    
    # Start the dashboard interface
    dashboard.run()

if __name__ == "__main__":
    main()
