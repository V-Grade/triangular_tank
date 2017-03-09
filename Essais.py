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

UtraSonicFrontal = 7
UtraSonicLateral = 4

#temps
temps90deg = 0.750

#distances
distanceFront = 0
distanceLateral = 0

#Directions de 1 a 4 dans le sens des aiguilles d'une montre
direction = 1 

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    bot.motorRun(MoteurAvant,0);
    bot.motorRun(MoteurArriere,0);
    sleep(0.05)
    bot.exiting=True
    quit()


bot = MegaPi()
bot.start('/dev/ttyUSB0')

signal.signal(signal.SIGINT, signal_handler)
#signal.pause()


#lecture des capteurs ultrasonic
def ReadUltra():
    bot.ultrasonicSensorRead(UtraSonicFrontal,onReadFront);
    bot.ultrasonicSensorRead(UtraSonicLateral,onReadLateral);

#r?cup?ration de la valeur de distance front
def onReadFront(v):
    global distanceFront
    distanceFront = v

#r?cup?ration de la valeur de distance Lat?rale
def onReadLateral(v):
    global distanceLateral
    distanceLateral = v

#tourner de 90? a gauche
def turnLeft():
    bot.motorRun(MoteurAvant,motorSpeed*coefRotation);
    bot.motorRun(MoteurArriere,motorSpeed*coefRotation);
    sleep(temps90deg)
    changeDirection(-1)

#tourner de 90? a droite
def turnRight():
    bot.motorRun(MoteurAvant,-motorSpeed*coefRotation);
    bot.motorRun(MoteurArriere,-motorSpeed*coefRotation);
    sleep(temps90deg)
    changeDirection(1)

#avancer tout droit
def avance(s=0.050):
    if not obstacleFront() :
        bot.motorRun(MoteurAvant,motorSpeed+coefCorection);
        bot.motorRun(MoteurArriere,-(motorSpeed-coefCorection));
        sleep(s)
    else:
        stop()

#stop
def stop():
    bot.motorRun(MoteurAvant,0);
    bot.motorRun(MoteurArriere,-(0));



#changement de direction
def changeDirection(d):
    global direction
    direction = direction + d
    if (direction > 4): direction = 1
    if (direction < 1): direction = 4

#d?tection d'obstacle frontale
def obstacleFront():
    return (distanceFront < 40) 

#d?tection d'obstacle lat?rale
def obstacleLateral():
    return (distanceLateral < 40)


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


if __name__ == '__main__':
    

    print 'initialisation'
    sleep(1);
    
    print 'lecture des capteurs de distances'
    ReadUltra()
    print distanceFront
    print distanceLateral
  
    sleep(2)
    
    print 'tourne a gauche'
    turnLeft()

    sleep(2)

    print 'tourne a droite'
    turnRight()

    sleep(2)

    print 'avance'
    avance()
    stop()

    sleep(1)    

    print 'avance pdt 1seconde'
    avance(1)
    stop()


    print 'wait for ctrl+C'
    sleep(10)

    print 'quit'
    quit()
