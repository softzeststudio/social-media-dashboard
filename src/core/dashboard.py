# src/core/dashboard.py

import curses
from core.api_manager import APIManager
from interfaces.tui_manager import TUIManager

class SocialMediaDashboard:
    def __init__(self, config):
        self.api_manager = APIManager(config)
        self.tui_manager = TUIManager(config)

    def run(self):
        curses.wrapper(self.tui_manager.display_dashboard, self.api_manager)
