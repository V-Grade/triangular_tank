#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megapi import *
import signal
import sys

# vitesses moteur
motorSpeed = 200 
coefCorection = 0.0 #correction de trajectiore
coefRotation = 0.5 #reduction de la vitesse pdt la rotation

#capteurs
MoteurAvant = M1
MoteurArriere = M2

#temps
temps90deg = 0.200

bot = MegaPi()
bot.start('/dev/ttyUSB0')

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    sleep(0.1)
    bot.exiting=True
    quit()

#tourner de 90? a gauche
def turnLeft():
    bot.motorRun(MoteurAvant,motorSpeed*coefRotation);
    bot.motorRun(MoteurArriere,motorSpeed*coefRotation);
    sleep(temps90deg)

#tourner de 90? a droite
def turnRight():
    bot.motorRun(MoteurAvant,-motorSpeed*coefRotation);
    bot.motorRun(MoteurArriere,-motorSpeed*coefRotation);
    sleep(temps90deg)

#stop
def stop():
    bot.motorRun(MoteurAvant,0);
    bot.motorRun(MoteurArriere,-(0));


if __name__ == '__main__':
    

    print 'initialisation'
    sleep(1);
    
    print 'tourne a gauche'
    turnLeft()

    sleep(2)

    print 'tourne a droite'
    turnRight()
    
    print 'signal'
    signal.signal(signal.SIGINT, signal_handler)

    sleep(2)
