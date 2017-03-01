from megapi import *

if __name__ == '__main__':
        bot = MegaPi()
        bot.start('/dev/ttyUSB0')
        bot.motorRun(M1,0);
        sleep(1);
        while 1:
                bot.motorRun(M1,200);
                bot.motorRun(M2,-200);
                bot.ultrasonicSensorRead(7,onRead);


def onRead(v):
	print "distance:"+str(v)+" cm";


