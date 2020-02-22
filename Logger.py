import sys
import argparse
import csv
import leather
import array
from time import localtime,strftime

from SoilModule import *
from THModule import *

def log(args):
    row = [strftime('%x %X')] #initalize row, starting with date & time cell
    with open('logs.csv', 'a', newline='') as csvfile:
        fwriter = csv.writer(csvfile)
        if args.All or args.atmosphere:
            thdata = readTHModule()
            row.append(thdata[0])
            row.append(thdata[1])
        else:
            row.append(0)
            row.append(0)
        if args.All or args.soil:
            smdata = readSoilMoisture()
            for x in smdata:
                row.append(x)
        print(row)
        fwriter.writerow(row)

def plot(col1, col2, start=0, end=0):
    cols = ['Time','Temperature','Humidity','Channel {} SoilMoisture'.format(col2-2)]
    data=[]
    dates=[]

    with open('logs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        i=0
        for row in reader:
            data.append((i,float(row[col2])))
            dates.append(row[0])
            i += 1
    print(data)
    def date_formatter(value, index, tick_count):
        return dates[index];
    chart = leather.Chart('{0} vs {1}'.format(cols[col1],cols[col2]))
    chart.add_x_axis(ticks = array.array('i',(i for i in range(start,end))), tick_formatter=date_formatter, name='Time')
    chart.add_y_axis(ticks = array.array('i',(5*i for i in range(0,19))))
    chart.add_x_scale(start,end)
    chart.add_y_scale(0, 90)
    chart.add_line(data)
    path = './images/{0}-{1}_{2}-{3}.svg'.format(cols[col1],cols[col2],start,end)
    chart.to_svg(path);
    return path

parser = argparse.ArgumentParser()
parser.add_argument('-s','--soil',help='log soil moisture',action='store_true')
parser.add_argument('-a','--atmosphere',help='log temperature & humidity',action='store_true')
parser.add_argument('-A','--All',help='log all sensors',action='store_true')
parsedargs = parser.parse_args()

log(parsedargs)
#plot(0,1,0,20)
