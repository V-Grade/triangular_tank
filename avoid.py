#!/usr/bin/env python

from megapi import *
import signal
import sys


front = 0
side = 0


def onReadFront(v):
    global front
    front = v
	#print "distance:"+str(v)+" cm";

def onReadSide(u):
    global side
    side = u


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sleep(0.05)
    bot.exiting=True
    quit()

def testCapteurFront ():
	
	while 1:
	   signal.signal(signal.SIGINT, signal_handler)
	   bot.ultrasonicSensorRead(7,onReadFront);
	   print front
	   sleep(0.1)

def testCapteurSide ():

        while 1:
           signal.signal(signal.SIGINT, signal_handler)
           bot.ultrasonicSensorRead(4,onReadSide);
           print side
	   sleep(0.1)

def pivoter():
    print 'tourner a gauche'
    bot.motorRun(M1,-100);
    bot.motorRun(M2,-100);
    sleep(1.355)
    print 'arret des moteurs'
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sleep(2)
    print 'tourner a droite'
    bot.motorRun(M1,100);
    bot.motorRun(M2,100);
    sleep(1.355)
    print 'arret des moteurs'
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);

def running():
    
	print("Press CTRL-C to stop.")
        while 1:
	   

	   signal.signal(signal.SIGINT, signal_handler)
	   bot.ultrasonicSensorRead(7,onReadFront);
	   sleep(0.05)
	   bot.ultrasonicSensorRead(4,onReadSide);
	   sleep(0.05)
	   print 'front distance:'
	   print front
	   print 'side distance'
	   print side
	   sleep(0.1)

	   if front > 50:
		print 'aller tout droit'
		bot.motorRun(M1,100);
		bot.motorRun(M2,-100);
		sleep(0.1)
            
	   elif front < 50 and side > 90:
		print 'tourner a droite' 
		bot.motorRun(M1,0);
		bot.motorRun(M2,0);
		bot.motorRun(M1,-100);
		bot.motorRun(M2,-100);
		sleep(0.1)
	   elif front < 50 and side < 90:
		print 'tourner a gauche'
		bot.motorRun(M1,0);
		bot.motorRun(M2,0);
		bot.motorRun(M1,100);
		bot.motorRun(M2,100);
		sleep(0.1)

           



if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    print 'initialisation'
    sleep(1)
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    print 'motors on run'
    
    try:
        running()
        
    except KeyboardInterrupt:
        print erreur
    
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sys.exit(0)
