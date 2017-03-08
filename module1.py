#!/usr/bin/env python

from megapi import *
import signal
import sys

def onRead(v):
    print ''
	#print "distance:"+str(v)+" cm";


def running():
    while 1:
        try:    

            sleep(0.5)
            bot.motorRun(M1,200);
            bot.motorRun(M2,-200);
            distance = bot.ultrasonicSensorRead(7);
            print distance
            

        except KeyboardInterrupt as erreur:
            bot.motorRun(M1,0);
            bot.motorRun(M2,0);          
            sys.exit(0)

    return


if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    bot.motorRun(M1,0);
    sleep(1);
    
    running()





