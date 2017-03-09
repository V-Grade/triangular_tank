#!/usr/bin/env python

from megapi import *
import signal
import sys


if __name__ == '__main__':
    bot = MegaPi()
    bot.start('/dev/ttyUSB0')
    bot.motorRun(M1,100);
    bot.motorRun(M2,100); 
    sleep(0.200)
sys.exit(0)
