import sys
import Adafruit_DHT

sensor = Adafruit_DHT.AM2303
pin = 15

humidity, temp = Adafruit_DHT.read_retry(sensor, pin) #read temp
temp = temp * 9/5.0 + 32 #convert celcius to fahrenheit

if humidity in not None and temp is not None:
    print('temp: {0:0.1f}f  humidity: {1:0.1f}%')
else:
    printerr('Failed to obtain am2303 reading')
    sys.exit(1)
