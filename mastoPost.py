from mastodon import Mastodon
import configparser
import sys

confParser = configparser.RawConfigParser()
confParser.read(r'growbot.conf')

apiURL = confParser.get('growbot-conf', 'apiURL')
clientSecret = 'growbot_client.secret'
userSecret = 'growbot_user.secret'

user = Mastodon(
    client_id = clientSecret,
    access_token = userSecret,
    api_base_url = apiURL
)

if len(sys.argv) < 3 :
    user.toot(sys.stdin.read())
#if len(sys.argv) == 2:

#if len(sys.argv) == 3:
else:
    sys.stderr.write('growbot-x: INVALID ARGUMENT FORMAT FOR MASTOPOST')
    exit(1)
