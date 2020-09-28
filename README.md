# growbot-x
Python scripts for growbox monitoring, federation, automation using the raspberry pi.

### Supported hardware:
- Raspberry pi
- Internet connection
- AM2302, DHT22, or DHT11 temperature/humidity sensor 
- MCP3008 A/D converter
- Capacitive soil moisture sensors (resistive sensors, while cheaper, corrode very quickly and are not suitable for this application)
- Pi Camera

Note: Due to the self-contained, modular nature of these scripts, you may choose to use only what sensors you need & their corresponding scripts.

If you have other hardware you would like to use, feel free to do so and help grow the project!

### Hardware Setup:
The temperature/humidity sensors are very simple to wire up. Just connect their power and ground to the respective pins on the pi, and connect data to any pin, though 3 is the default here (this shows up as 2 in the config because it is 0 indexed).

The MCP3008 is a little trickier, I will add a diagram here at a later date.

The soil moisture sensors can be connected almost just like the temp/humidity sensors, except data will go to one of the channel pins on the MCP3008.

### Software Dependecies:
- Python 3
- Pip3
- Adafruit_DHT (install using 'sudo pip3 install Adafruit_DHT', requires pip)
- Spidev-py (install using 'sudo pip3 install spidev, requires pip)
- Mastodon.py (install using 'sudo pip3 install Mastodon.py, requires pip)
- RPi.GPIO (install using 'sudo pip3 install RPi.GPIO, requires pip)

## Getting Started:
After installing and setting up Raspbian on you pi (including network configuration and __enabling SPI__), __install Python3, pip3, & depedencies__ ('sudo pip3 install Adafruit_DHT spidev Mastodon.py RPi.GPIO'). __Make an account__ on any ActivityPub server which supports the MastodonAPI, (i.e. Pleroma, Mastodon, etc.) Next, __copy conf.example (the example config) to conf.secret__ and then __edit conf.secret__ by filling in the URL for the instance you chose as well as details about your hardware. Finally, simply __run 'python3 generateSecrets.py'__.


## Usage:
To post all sensor readings, use 'python3 mastoPost.py -A', for more options, read 'python3 mastoPost.py -h'
Additionally, any script may be run individually i.e. 'python3 THModule.py'. These outputs can be piped into mastoPost.py like so 'python3 THModule.py | python3 mastoPost.py'.
Automation of the scripts is as simple as setting up a cronjob.
