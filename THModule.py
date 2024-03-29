import sys
import Adafruit_DHT
import configparser
import os

def readTHModule():
    confFile = os.path.join(os.path.dirname(__file__), 'conf.secret')
    confParser = configparser.RawConfigParser()
    confParser.read(confFile)

    sensorModel = confParser.get('growbot-conf', 'temp_humidity_sensor')
    pin = confParser.getint('growbot-conf', 'temp_humidity_pin')
    sensor = None
    if sensorModel == 'AM2302': 
            sensor = Adafruit_DHT.AM2302
    elif sensorModel == 'DHT22':
            sensor = Adafruit_DHT.DHT22
    elif sensorModel == 'DHT11':
            sensor = Adafruit_DHT.DHT11
    else:
            sys.stderr.write('growbot-x: INVALID SENSOR TYPE IN CONFIG - i.e. AM2303, DHT22, DHT11' + sensorModel)
            exit(1)

    humidity, temp = Adafruit_DHT.read_retry(sensor, pin) #read temp

    if humidity is not None and temp is not None:
        temp = temp * 9/5.0 + 32 #convert celcius to fahrenheit
        return(['{0:0.1f}'.format(temp),'{0:0.1f}%'.format(humidity)])
    else:
        raise Exception('Failed to obtain temperature & humidity reading')
