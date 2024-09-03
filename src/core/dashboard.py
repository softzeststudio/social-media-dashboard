# src/core/dashboard.py

import curses
from core.api_manager import APIManager
from core.authentication import AuthenticationManager
from platforms.twitter import TwitterAPI
from platforms.reddit import RedditAPI
from platforms.mastodon import MastodonAPI


class SocialMediaDashboard:
    def __init__(self, config):
        self.api_manager = APIManager(config)
        self.tui_manager = TUIManager(config)

    def run(self):
        curses.wrapper(self.tui_manager.display_dashboard, self.api_manager)
