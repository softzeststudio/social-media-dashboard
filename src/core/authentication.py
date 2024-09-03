# src/core/authentication.py

import tweepy
import praw
from mastodon import Mastodon

class AuthenticationManager:
    def __init__(self, credentials):
        self.credentials = credentials

    def authenticate_twitter(self):
        auth = tweepy.OAuthHandler(
            self.credentials['twitter']['api_key'],
            self.credentials['twitter']['api_secret_key']
        )
        auth.set_access_token(
            self.credentials['twitter']['access_token'],
            self.credentials['twitter']['access_token_secret']
        )
        return tweepy.API(auth)

    def authenticate_reddit(self):
        return praw.Reddit(
            client_id=self.credentials['reddit']['client_id'],
            client_secret=self.credentials['reddit']['client_secret'],
            user_agent=self.credentials['reddit']['user_agent']
        )

    def authenticate_mastodon(self):
        return Mastodon(
            client_id=self.credentials['mastodon']['client_id'],
            client_secret=self.credentials['mastodon']['client_secret'],
            access_token=self.credentials['mastodon']['access_token'],
            api_base_url=self.credentials['mastodon']['api_base_url']
        )

        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)

    @staticmethod
    def reddit_auth(client_id, client_secret, user_agent, username, password):
        return praw.Reddit(client_id=client_id,
                           client_secret=client_secret,
                           user_agent=user_agent,
                           username=username,
                           password=password)

    @staticmethod
    def mastodon_auth(client_id, client_secret, access_token, api_base_url):
        return Mastodon(client_id=client_id, client_secret=client_secret, access_token=access_token, api_base_url=api_base_url)
