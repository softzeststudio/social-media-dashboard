# src/tests/test_api_manager.py

import unittest
from core.api_manager import APIManager
from core.config_manager import ConfigManager

class TestAPIManager(unittest.TestCase):
    def setUp(self):
        self.config = ConfigManager.load_config('config/default_config.yaml')
        self.api_manager = APIManager(self.config)

    def test_fetch_feeds(self):
        feeds = self.api_manager.fetch_feeds()
        self.assertIn('twitter', feeds)
        self.assertIn('reddit', feeds)
        self.assertIn('mastodon', feeds)

if __name__ == '__main__':
    unittest.main()
