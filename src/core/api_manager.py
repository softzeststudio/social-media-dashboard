# src/core/api_manager.py

from platforms.twitter import TwitterAPI
from platforms.reddit import RedditAPI
from platforms.mastodon import MastodonAPI

class APIManager:
    def __init__(self, config):
        self.twitter_api = TwitterAPI(config['twitter'])
        self.reddit_api = RedditAPI(config['reddit'])
        self.mastodon_api = MastodonAPI(config['mastodon'])

    def fetch_feeds(self):
        twitter_feed = self.twitter_api.get_feed()
        reddit_feed = self.reddit_api.get_feed()
        mastodon_feed = self.mastodon_api.get_feed()

        return {
            'twitter': twitter_feed,
            'reddit': reddit_feed,
            'mastodon': mastodon_feed
        }
