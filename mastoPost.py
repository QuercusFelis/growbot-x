from mastodon import Mastodon
import configparser
import argparse
import sys

import SoilMoisture.py
import THModule.py
import CameraModule.py

confParser = configparser.RawConfigParser()
confParser.read(r'conf.secret')

parser = argparse.ArgumentParser()
parser.add_argument('-s','--soil',help='read soil moisture',action='store_true')
parser.add_argument('-a','--atmosphere',help='read temperature & humidity',action='store_true')
parser.add_argument('-c','--camera',help='take a photo',action='store_true')
parser.add_argument('-A','--All',help='poll camera and all sensors',action='store_true')
args = arser.parse_args()

apiURL = confParser.get('growbot-conf', 'apiURL')
clientSecret = 'growbot_client.secret'
userSecret = 'growbot_user.secret'
username = confParser.get('growbot-conf', 'username')
password = confParser.get('growbot-conf', 'password')
user = Mastodon(
    client_id = clientSecret,
    api_base_url = apiURL
)
user.log_in(username, password, to_file=userSecret)
user = Mastodon(
        access_token = userSecret,
        api_base_url = apiURL
)

outstr = ''
#if String.len() != 0 :
#    print('['+outstr+']')
#    outstr += sys.stdin.read() + '\n\n'
if args.All or args.atmosphere:
    outstr += readTHModule()
if args.All or args.soil:
    outstr += readSoilMoisture()
if args.All or args.camera:
    user.status_post(
        outstr, 
        media_ids=user.media_post(photo()))
    exit(0)
else:
    sys.stderr.write('growbot-x: INVALID ARGUMENT FORMAT FOR MASTOPOST\n')
    exit(1)
user.status_post(outstr)
exit(0)
