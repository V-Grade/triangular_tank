#!/usr/bin/env python

from megapi import *
import signal
import sys


front = 0
side = 0
direction= 1

def onReadFront(v):
    global front
    front = v


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

#tourner de 90? a gauche
def turnLeft():
    print 'gauche'
    bot.motorRun(M1,100);
    bot.motorRun(M2,100);
    sleep(1.150)
    changeDirection(-1)

#tourner de 90? a droite
def turnRight():
    print 'droite'
    bot.motorRun(M1,-100);
    bot.motorRun(M2,-100);
    sleep(1.150)
    changeDirection(1)

#avancer tout droit
def avance(s=0.1):
    if not obstacleFront() :
        bot.motorRun(M1,100);
        bot.motorRun(M2,-100);
        sleep(s)
    else:
        stop()

#stop
def stop():
    print 'stop'
    bot.motorRun(M1,0);
    bot.motorRun(M2,-(0));



#changement de direction
def changeDirection(d):
    global direction
    direction = direction + d
    if (direction > 4): direction = 1
    if (direction < 1): direction = 4

#d?tection d'obstacle frontale
def obstacleFront():
    return (front < 20) 

#d?tection d'obstacle lat?rale
def obstacleLateral():
    return (side < 20)


#tourner dans la meilleur direction
def Tourne():
    # tourne a gauche si on est dans la direction Nord
    if direction == 1 :
        turnLeft()
    # fait demis tour si on est dans la direction Ouest
    elif direction == 4 :
        turnRight()
        turnRight()
    #tourne a gauche si on est dans la direction Est
    elif direction == 2 :
        turnLeft()


def running():
    print("Press CTRL-C to stop.")
    i=0
    while front==0:
    	signal.signal(signal.SIGINT, signal_handler)
    	print 'light:'
    	i=i+1
    	bot.rgbLedSetColor(6, 1, i, 200, 10, 10)
    	if(i>=12): i=1;
    	bot.ultrasonicSensorRead(7,onReadFront);
    	sleep(0.05)
    	bot.ultrasonicSensorRead(4,onReadSide);
    	sleep(0.05)
    	print 'front distance:'
    	print front
    	print 'side distance'
    	print side
    	sleep(0.1)
    sleep(1)
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

        # rien a droite lord du d?placement vers l'Ouest
        if (not obstacleLateral() and direction == 4 ):
	        avance(0.8)
	        turnRight()
        # qq chose devant
        elif (obstacleFront()):
	        Tourne()
        # sinon
        else:
	        avance()


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
