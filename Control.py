import RPi.GPIO as GPIO
import configparser
import argparse
import sys

from SoilModule import *
from THModule import *

# Read in arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l','--lights',help='set lights on/off (i.e. -l on, -l off)')
parser.add_argument('-p','--pump',help='control pump from soil moisture (NOT IMPLEMENTED)',action='store_true')
parser.add_argument('-t','--temp',help='Attempt to heat or cool to given temperature (i.e. -t 75)')
parser.add_argument('-h','--humidity',help='control humidity from humidity sensor (NOT IMPLEMENTED)',action='store_true')
args = parser.parse_args()

# if called directly
control();

def control():
    confParser = initControl()
    if args.lights:
        setLights(args.lights)
    if args.temp:
        setTemp(args.temp)

def initControl():
    confParser = configparser.RawConfigParser()
    confParser.read(r'conf.secret')
    GPIO.setmode(GPIO.BOARD)
    return confParser

def setLights(setting):
    confParser = initControl()
    pin = confParser.getint('growbot-conf', 'GPIO-pin-light')
    GPIO.setup(pin, GPIO.OUT)

    if setting == 'on':
        GPIO.output(pin, 1)
    else:
        GPIO.output(pin, 0)

def setTemp(setting):
    confParser = initControl()
    pin = confParser.getint('growbot-conf', 'GPIO-pin-temp')
    heat = confParser.getboolean('growbot-conf', 'heater')
    GPIO.setup(pin, GPIO.OUT)

    temp = readTHModule()[0]
    if (temp < setting && heat) or (temp > setting && !heat):
        GPIO.output(pin, 1)
    else:
        GPIO.output(pin, 0)

def setPin(pin, setting):
    initControl()
    GPIO.setup(pin, OUT)
    GPIO.output(pin, setting)

exit(0)
