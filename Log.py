import sys
import argparse
import csv
import matplotlib.pyplot as plt
from time import localtime,strftime

import SoilMoisture.py
import THModule.py

confParser = configparser.RawConfigParser()
confParser.read(r'conf.secret')

parser = argparse.ArgumentParser()
parser.add_argument('-s','--soil',help='log soil moisture',action='store_true')
parser.add_argument('-a','--atmosphere',help='log temperature & humidity',action='store_true')
parser.add_argument('-A','--All',help='log all sensors',action='store_true')
parsedargs = arser.parse_args()

log(parsedargs)

def log(args):
    row = [strftime('%x %X')] #initalize row, starting with date & time cell
    with open('logs.csv', 'wb') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)

        if args.All or args.atmosphere:
            thdata = readTHModule()
            row.append(thdata[0])
            row.append(thdata[1])
        if args.All or args.soil:
            smdata = readSoilMoisture()
            for x in smdata:
                row.append(x)

        fwriter.writerow(row)

def plot(col1, col2, start=0, end=0):
    cols = ['Time','Temperature','Humidity','Channel {} SoilMoisture'.format(col2-2)]
    x=[]
    y=[]

    with open('logs.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in range(start,end):
            x.append(int(data[i][col1]))
            y.append(int(data[i][col2]))
    plt.plot(x,y,marker='o')
    plt.title(cols[col1]+' vs '+cols[col2])
    plt.xlabel(cols[col1])
    plt.ylabel(cols[col2])
    path = './images/{0}-{1}_{2}-{3}.png'.format(cols[col1],cols[col2],start,end)
    plt.savefig(path)
    return path
