# API Keys Setup

To use the social media dashboard, you'll need to obtain API keys for each platform.

## Twitter
1. Go to the [Twitter Developer Portal](https://developer.twitter.com/).
2. Create a new app and generate the following keys:
    - Consumer Key
    - Consumer Secret
    - Access Token
    - Access Token Secret

3. Copy these keys into the `twitter` section of `config/user_config.yaml`.

## Reddit
1. Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps).
2. Create a new app and note down the following:
    - Client ID
    - Client Secret

3. Update the `reddit` section of `config/user_config.yaml` with these values.

## Mastodon
1. Go to your Mastodon instance and create a new application under preferences.
2. Generate the following:
    - Client ID
    - Client Secret
    - Access Token

3. Copy these keys into the `mastodon` section of `config/user_config.yaml`.

## Additional Notes
- Keep your API keys secure and do not share them publicly.
- For more details, refer to the documentation of each platform.
