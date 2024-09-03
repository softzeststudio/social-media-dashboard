# src/platforms/reddit.py

from core.authentication import AuthenticationManager

class RedditAPI:
    def __init__(self, config):
        self.reddit = AuthenticationManager.reddit_auth(config['client_id'], config['client_secret'],
                                                        config['user_agent'], config['username'], config['password'])

    def get_feed(self, subreddit='all', limit=5):
        posts = self.reddit.subreddit(subreddit).hot(limit=limit)
        return [{'title': post.title, 'author': post.author.name} for post in posts]
