from mastodon import Mastodon
import configparser

confParser = configparser.RawConfigParser()
confParser.read(r'growbot.conf')

apiURL = confParser.get('growbot-conf', 'apiURL')
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

user.toot('Beep Boop. Your bot is ready :D')
