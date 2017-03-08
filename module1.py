#!/usr/bin/env python

from megapi import *
import signal
import sys

def onRead(v):
	print "distance:"+str(v)+" cm";


def running():
    while 1:
        try:    

            sleep(0.5)
            bot.motorRun(M1,200);
            bot.motorRun(M2,-200);
            distance = bot.ultrasonicSensorRead(7);
            print distance
            

        except KeyboardInterrupt as erreur:
            return

    return


if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    bot.motorRun(M1,0);
    sleep(1);
    
    running()





