# src/platforms/mastodon.py

from core.authentication import AuthenticationManager

class MastodonAPI:
    def __init__(self, config):
        self.mastodon = AuthenticationManager.mastodon_auth(config['client_id'], config['client_secret'],
                                                            config['access_token'], config['api_base_url'])

    def get_feed(self, limit=5):
        toots = self.mastodon.timeline_home(limit=limit)
        return [{'account': toot['account']['username'], 'content': toot['content']} for toot in toots]
