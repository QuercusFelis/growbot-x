from mastodon import Mastodon
import configparser
import argparse
import sys
import os

import SoilModule as soilmodule
from THModule import readTHModule
from CameraModule import photo
#import Logger

confFile = os.path.join(os.path.dirname(__file__), 'conf.secret')
confParser = configparser.RawConfigParser()
confParser.read(confFile)

# Read in arguments
parser = argparse.ArgumentParser()
parser.add_argument('-s','--soil',help='read soil moisture',action='store_true')
parser.add_argument('-a','--atmosphere',help='read temperature & humidity',action='store_true')
parser.add_argument('-c','--camera',help='take a photo',action='store_true')
parser.add_argument('-A','--All',help='poll camera and all sensors',action='store_true')
args = parser.parse_args()

# Login
apiURL = confParser.get('growbot-conf', 'apiURL')
clientSecret = os.path.join(os.path.dirname(__file__), 'growbot_client.secret')
userSecret = os.path.join(os.path.dirname(__file__), 'growbot_user.secret')
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

# Format data and post it
outstr = ''
if args.All or args.atmosphere:
    thmod = readTHModule()
    outstr += 'Temp: '+thmod[0]+'f'
    outstr += '  '
    outstr += 'Humidity: '+thmod[1]+'\n\n'
if args.All or args.soil:
    smmod = soilmodule.readSoilMoisture()
    for i in range(len(smmod)-1):
        outstr += '['+i+'] '+smmod[i]+'\n'
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
