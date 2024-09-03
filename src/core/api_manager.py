# src/core/api_manager.py

from platforms.twitter import TwitterAPI
from platforms.reddit import RedditAPI
from platforms.mastodon import MastodonAPI

class APIManager:
    def __init__(self, credentials):
        self.twitter_api = TwitterAPI(credentials)
        self.reddit_api = RedditAPI(credentials)
        self.mastodon_api = MastodonAPI(credentials)

    def post_to_twitter(self, message):
        self.twitter_api.post_tweet(message)

    def post_to_reddit(self, message):
        self.reddit_api.submit_post(message)

    def post_to_mastodon(self, message):
        self.mastodon_api.toot(message)
