# src/platforms/twitter.py

from core.authentication import AuthenticationManager
import tweepy

class TwitterAPI:
    def __init__(self, credentials):
        self.auth_manager = AuthenticationManager(credentials)
        self.api = self.auth_manager.authenticate_twitter()

    def get_feed(self, count=5):
        tweets = self.api.home_timeline(count=count)
        return [{'user': tweet.user.name, 'text': tweet.text} for tweet in tweets]
    def post_tweet(self, message):
        self.api.update_status(message)
