# src/core/authentication.py

import tweepy
import praw
from mastodon import Mastodon

class AuthenticationManager:
    @staticmethod
    def twitter_auth(consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
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
