#!/usr/bin/env python

from megapi import *
import signal
import sys

def onRead(v):
	print "distance:"+str(v)+" cm";

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()


if __name__ == '__main__':
        bot = MegaPi()
        bot.start('/dev/ttyUSB0')
        bot.motorRun(M1,0);
        sleep(1);
        while 1:
                bot.motorRun(M1,200);
                bot.motorRun(M2,-200);
                bot.ultrasonicSensorRead(7,onRead);


