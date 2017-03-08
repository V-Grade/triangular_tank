#!/usr/bin/env python

from megapi import *
import signal
import sys


distance = 0


def onRead(v):
    distance = v
	#print "distance:"+str(v)+" cm";


def running():
    
        print("Press CTRL-C to stop.")
        while 1:
            sleep(0.5)
            bot.motorRun(M1,200);
            bot.motorRun(M2,-200);
            bot.ultrasonicSensorRead(7,onRead);
            print distance



if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    print 'initialisation'
    sleep(1);
    try:
        running()
    except KeyboardInterrupt as erreur:
        print 'ctrl+c'
        bot.motorRun(M1,0);
        bot.motorRun(M2,0); 
        sys.exit(0)




