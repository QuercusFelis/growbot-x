from mastodon import Mastodon
import sys

apiURL = 'https://wetfish.space'
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
    print('growbotx: INVALID ARGUMENT FORMAT')
