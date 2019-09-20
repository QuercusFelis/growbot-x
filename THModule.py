import sys
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4

humidity, temp = Adafruit_DHT.read_retry(sensor, pin) #read temp

if humidity is not None and temp is not None:
    temp = temp * 9/5.0 + 32 #convert celcius to fahrenheit
    print('temp: {0:0.1f}f  humidity: {1:0.1f}%'.format(temp, humidity))
else:
    sys.stderr.write('Failed to obtain am2303 reading\n')
    sys.exit(1)
