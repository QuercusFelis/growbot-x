from mastodon import Mastodon

apiURL = input('Please type the full URL of your instance: ')
username = input('Username: ')
password = input('Password: ')
clientSecret = 'growbot_client.secret'
userSecret = 'growbot_user.secret'

Mastodon.create_app(
    'growbot-x',
    api_base_url = apiURL,
    to_file = clientSecret
)

user = Mastodon(
    client_id = clientSecret,
    api_base_url = apiURL
)

user.log_in(
    username,
    password,
    to_file = userSecret
)

user.toot('This is a test of the growbox-x alert subsystem (that\'s fancy speak for pleroma bot)')
