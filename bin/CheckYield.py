#! /usr/bin/env python

import sys
import os

pypath= os.path.realpath(__file__) 
print sys.argv[0]
dirpath=os.path.dirname(pypath)
sys.path.insert(0,dirpath+'/../python/')
from Utils import *


if __name__ == '__main__':
    #inputpath,processlist
    inputpath=sys.argv[1]
    processlist=[sys.argv[2]]
    Y=ReadYield(inputpath,processlist)
    #ReadYield
    print Y
