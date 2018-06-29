# by Joh Schoeneberg 2018
# All rights reserved

import lvm_read
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import os
import datetime
import pandas as pd



def readForceFile(filename):
    lvm = lvm_read.read(filename, read_from_pickle=False)
    #print(lvm['Description'])

    datetime = getLVMdatetime(lvm[0]['Time'][0],lvm[0]['Date'][0])

    data = lvm[0]['data']
    t = data[:,0]
    x = data[:,1]
    y = data[:,2]
    xforceraw = data[:,3]
    yforceraw = data[:,4]

    return [t,x,y,datetime,xforceraw,yforceraw]


def getLVMdatetime(lvmTimeString,lvmDateString):
    dateString = lvmDateString
    dateSplit=dateString.split('/')


    timeString = lvmTimeString
    timeSplit=timeString.split(':')

    #test = datetime.datetime(2017, 6, 26, 18, 21, 16, 533499)
    # this is the time the file was r
    test = datetime.datetime(int(dateSplit[0]),
                         int(dateSplit[1]),
                         int(dateSplit[2]),
                         int(timeSplit[0]),
                         int(timeSplit[1]),
                         int(timeSplit[2].split('.')[0]),
                        0)

    #print(test.strftime('%Y-%m-%d %H:%M:%S'))
    return test
