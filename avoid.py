#!/usr/bin/env python

from megapi import *
import signal
import sys


frontDistance = 0
sideDistance = 0


def onReadFront(v):
    global frontDistance
    frontDistance = v
	#print "distance:"+str(v)+" cm";

def onReadSide(u):
    global sideDistance
    sideDistance = u


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sleep(0.05)
    bot.exiting=True
    quit()


def testUtrasonic():

	while 1:
	   bot.ultrasonicSensorRead(7,onReadFront);
           bot.ultrasonicSensorRead(4,onReadSide);
	   print frontDistance
	   print sideDistance
	   print 'again'
	   signal.signal(signal.SIGINT, signal_handler)

def running():
    
	print("Press CTRL-C to stop.")
        while 1:
	    
	    signal.signal(signal.SIGINT, signal_handler)
	    bot.ultrasonicSensorRead(7,onReadFront);
            bot.ultrasonicSensorRead(4,onReadSide);

            print frontDistance
	    print sideDistance
            if frontDistance > 20:
                 bot.motorRun(M1,200);
                 bot.motorRun(M2,-200);
		 sleep(0.1);
            
            elif frontDistance < 20 and sideDistance > 20: 
                 bot.motorRun(M1,0);
                 bot.motorRun(M2,0);
	         bot.motorRun(M1,-100);
                 bot.motorRun(M2,-100);
		 sleep(0.1);
	    else frontDistance < 20 and sideDistance < 20:
		 bot.motorRun(M1,0);
                 bot.motorRun(M2,0); 
		 bot.motorRun(M1,100);
                 bot.motorRun(M2,100);
		 sleep(0.1);

           



if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    print 'initialisation'
    sleep(1);
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    print 'motors on run'
    
    try:
        testUtrasonic()
        
    except KeyboardInterrupt:
        print erreur
    
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sys.exit(0)
