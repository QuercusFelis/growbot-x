from mastodon import Mastodon
import configparser
import argparse
import sys

import SoilMoisture.py
import THModule.py
import CameraModule.py

confParser = configparser.RawConfigParser()
confParser.read(r'growbot.conf')

parser = argparse.ArgumentParser()
parser.add_argument('-s','--soil',help='read soil moisture',action='store_true')
parser.add_argument('-a','--atmosphere',help='read temperature & humidity',action='store_true')
parser.add_argument('-c','--camera',help='take a photo',action='store_true')
parser.add_argument('-A','--All',help='poll camera and all sensors',action='store_true')
args = arser.parse_args()

stdin = sys.stdin.read()

apiURL = confParser.get('growbot-conf', 'apiURL')
clientSecret = 'growbot_client.secret'
userSecret = 'growbot_user.secret'
user = Mastodon(
    client_id = clientSecret,
    access_token = userSecret,
    api_base_url = apiURL
)

outstr = ''
if String.len(stdin) != 0 :
    outstr += sys.stdin.read() + '\n\n'
if args.All||args.atmosphere:
    outstr += THModule.readTHModule()
if args.All||args.soil:
    outstr += SoilMoisture.readSoilMoisture()
if args.All||args.camera:
    user.status_post(
        outstr, 
        media_ids=user.media_post(CameraModule.photo()))
    exit(0)
else:
    sys.stderr.write('growbot-x: INVALID ARGUMENT FORMAT FOR MASTOPOST')
    exit(1)
user.toot(outstr)
exit(0)
