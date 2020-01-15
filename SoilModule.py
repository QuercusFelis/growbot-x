import sys
import configparser
import spidev

confParser = configparser.RawConfigParser()
confParser.read(r'growbot.conf')

numChannels = confParser.getint('growbot-conf', 'mcp3008_channels')

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz(confParser.getint('growbot-conf', 'spi_freq'))

outStr = ''
for i in range (0,numChannels-1)
    spi.cshigh = false
    chan = hex(i)+0x18 #first digit is start bit, second tells a/d to use non-differential mode i.e. 0b00011XXX
    spi.xfer([0x0,chan])
    percentage = 100*(spi.readbytes(2)/1024) #mcp gives 10-bit output, so top 6 bits are 'empty'
    spi.cshigh = true
    outstr += i + ': ' + percentage + '% '

print(outStr)
exit(0)