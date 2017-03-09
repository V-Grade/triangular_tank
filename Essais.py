
temps90deg = 1250

#distances
distanceFront = 0
distanceLateral = 0

#Directions de 1 a 4 dans le sens des aiguilles d'une montre
direction = 1 

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    bot.motorRun(M1,0);
    bot.motorRun(M2,0);
    quit()

signal.signal(signal.SIGINT, signal_handler)
signal.pause()


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
    bot.motorRun(M1,motorSpeed*coefRotation);
    bot.motorRun(M2,motorSpeed*coefRotation);
    sleep(temps90deg)
    changeDirection(-1)

#tourner de 90? a droite
def turnRight():
    bot.motorRun(M1,-motorSpeed*coefRotation);
    bot.motorRun(M2,-motorSpeed*coefRotation);
    sleep(temps90deg)
    changeDirection(1)

#avancer tout droit
def avance(s=0.050):
    if not obstacleFront() :
        bot.motorRun(M1,motorSpeed+coefCorection);
        bot.motorRun(M2,-(motorSpeed-coefCorection));
        sleep(s)
    else:
        stop()

#stop
def stop():
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
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
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

