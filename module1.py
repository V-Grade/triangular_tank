from megapi import *

if __name__ == '__main__':
        bot = MegaPi()
        bot.start('/dev/ttyUSB0')
        bot.motorRun(M1,0);
        sleep(1);
        while 1:
                sleep(1);
                bot.motorRun(M1,50);
                bot.motorRun(M2,-50);
                bot.ultrasonicSensorRead(7,onRead);
                sleep(1);
                bot.motorRun(M1,0);
                bot.motorRun(M2,-0);
                bot.ultrasonicSensorRead(7,onRead);
                sleep(1);
                bot.motorRun(M1,-50);
                bot.motorRun(M2,50);
                bot.ultrasonicSensorRead(7,onRead);
                sleep(1);
                bot.motorRun(M1,0);
                bot.motorRun(M2,-0);
                bot.ultrasonicSensorRead(7,onRead);

		        


def onRead(v):
	print "distance:"+str(v)+" cm";


