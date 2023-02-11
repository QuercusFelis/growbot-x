import sys
import configparser
import spidev
import os

def readSoilMoisture():
    confFile = os.path.join(os.path.dirname(__file__), 'conf.secret')
    confParser = configparser.RawConfigParser()
    confParser.read(confFile)

    numChannels = confParser.getint('growbot-conf', 'mcp3008_channels')
    raw = confParser.getboolean('growbot-conf', 'soil_moisture_raw_output')
    offset = confParser.getint('growbot-conf', 'soil_moisture_offset')
    scale = confParser.getfloat('growbot-conf', 'soil_moisture_scale_factor')

    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = confParser.getint('growbot-conf', 'spi_freq')

    outputs = []
    for i in range (numChannels):
        # First bit is start bit, Second bit indicates non-differential mode, Last 3 are pin select (i)
        reading = spi.xfer2([0x1, (0x8+i) << 4, 0x0]) # Raw binary output from MCP3008
        value = (reading[1]%4 << 8) + reading[2] # Convert to a raw decimal value (0-1023)
        value = (value - offset) * scale # Correct value
        if raw:
            outputs.append(value)
        else:
            percent = 100*(value/1023) # Convert to a percentage (0-100)
            outputs.append('{1:.2f}%'.format(percent))
    return outputs
