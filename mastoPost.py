from mastodon import Mastodon

Mastodon.create_app(
    'growbot-x',
    api_base_url = 'https://wetfish.space',
    to_file = 'growbot_client.secret'
)

user = Mastodon(
    access_token = 'growbot_client.secret',
    api_base_url = 'https://wetfish.space'
)

user.log_in(
    to_file = 'growbot_client.secret'
)

user.toot('This is a test of the growbox-x alert subsystem (that\'s fancy speak for pleroma bot)')
