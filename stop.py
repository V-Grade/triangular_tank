#!/usr/bin/env python

from megapi import *
import signal
import sys


if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    bot.motorRun(M1,0);
    bot.motorRun(M2,0); 
    sys.exit(0)





