from mastodon import Mastodon
import configparser

confParser = configparser.RawConfigParser()
confParser.read(r'conf.secret')

apiURL = confParser.get('growbot-conf', 'apiURL')
username = confParser.get('growbot-conf', 'username')
password = confParser.get('growbot-conf', 'password')
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
print('Beep Boop. Your bot is ready :D')
exit(0)
