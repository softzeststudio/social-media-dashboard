# src/core/config_manager.py

import yaml

class ConfigManager:
    @staticmethod
    def load_config(config_file="config/user_config.yaml"):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config

    @staticmethod
    def save_config(config, config_file="config/user_config.yaml"):
        with open(config_file, 'w') as file:
            yaml.safe_dump(config, file)
