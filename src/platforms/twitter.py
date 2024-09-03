# src/platforms/twitter.py

from core.authentication.py import AuthenticationManager

class TwitterAPI:
    def __init__(self, config):
        self.api = AuthenticationManager.twitter_auth(config['consumer_key'], config['consumer_secret'],
                                                      config['access_token'], config['access_token_secret'])

    def get_feed(self, count=5):
        tweets = self.api.home_timeline(count=count)
        return [{'user': tweet.user.name, 'text': tweet.text} for tweet in tweets]
