from core.api_manager import APIManager

class SocialMediaDashboard:
    def __init__(self, credentials):
        self.api_manager = APIManager(credentials)

    def post_to_all(self, message):
        self.api_manager.post_to_twitter(message)
        self.api_manager.post_to_reddit(message)
        self.api_manager.post_to_mastodon(message)
