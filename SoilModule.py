import sys
import configparser
import spidev

def readSoilMoisture():
    confParser = configparser.RawConfigParser()
    confParser.read(r'conf.secret')

    numChannels = confParser.getint('growbot-conf', 'mcp3008_channels')

    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = confParser.getint('growbot-conf', 'spi_freq')

    percents = []
    for i in range (numChannels):
        chan = i+0x18 #first digit is start bit, second tells a/d to use non-differential mode i.e. 0b00011XXX
        reading = spi.xfer2([0x1, (0x8+i) << 4, 0x0])
        value = (reading[1]%4 << 8)+reading[2]-445
        percent = 100*(445-value)/445
        percents.append('{0:.2f}%'.format(percent))
    return percents;
