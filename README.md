# growbot-x
Python scripts for growbox monitoring, federation, automation using the raspberry pi.

### Required hardware:
- Raspberry pi
- Internet connection
- AM2302, DHT22, or DHT11 temperature/humidity sensor 
- MCP3008 A/D converter
- Capacitive soil moisture sensors
- Pi Camera

Note: Due to the self-contained, modular nature of these scripts, you may choose to use only what sensors you need & their corresponding scripts.

### Hardware Setup:
The temperature/humidity sensors are very simple to wire up. Just connect their power and ground to the respective pins on the pi, and connect data to any pin, though 2 is the default here.

The MCP3008 is a little trickier, I will add a diagram here at a later date.

The soil moisture sensors can be connected almost just like the temp/humidity sensors, except data will go to one of the channel pins on the MCP3008.

### Software Dependecies:
- Python 3
- Adafruit_DHT (install using 'sudo pip3 install Adafruit_DHT', requires pip)

## Getting Started:
First install Python 3 & Adafruit_DHT. Next, edit growbot.conf. Finally, if you are federating your bot, run 'python3 generateSecrets.py' and follow the instructions there.

## Usage:
To use, any script may be run individually i.e. 'python3 THModule.py', or if you are federating you can pass this output through stdin to mastoPost.py simply by doing 'python3 THModule.py | python3 mastoPost.py'. Automation of script running is as simple as setting up a cronjob.
