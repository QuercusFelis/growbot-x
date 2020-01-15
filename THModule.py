import sys
import Adafruit_DHT
import configparser

confParser = configparser.RawConfigParser()
confParser.read(r'growbot.conf')

sensorModel = confParser.get('growbot-conf', 'temp_humidity_sensor')
pin = confParser.getint('growbot-conf', 'temp_humidity_pin')
sensor = None
switch(sensorModel)
{
    case 'AM2302': 
        sensor = Adafruit_DHT.AM2302
        break;
    case 'DHT22':
        sensor = Adafruit_DHT.DHT22
        break;
    case 'DHT11':
        sensor = Adafruit_DHT.DHT11
        break;
    default:
        sys.stderr.write('growbot-x: INVALID SENSOR TYPE IN CONFIG - i.e. AM2303, DHT22, DHT11')
        exit(1)
}

humidity, temp = Adafruit_DHT.read_retry(sensor, pin) #read temp

if humidity is not None and temp is not None:
    temp = temp * 9/5.0 + 32 #convert celcius to fahrenheit
    print('temp: {0:0.1f}f  humidity: {1:0.1f}%'.format(temp, humidity))
    sys.exit(0)
else:
    sys.stderr.write('growbot-x: Failed to obtain temperature & humidity reading\n')
    sys.exit(2)
