# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:29:29 2018

@author: admin
"""

import time

strtime = '2017-08-21 10:54:31'

starttime = time.time()

i=0

while i<100000:
    stra = time.strptime(strtime, '%Y-%m-%d %H:%M:%S')
    i += 1
    
endtime = time.time()

print("time parse used {}".format(endtime-starttime))


starttime = time.time()

i=0

while i<100000:
    stra = strtime[5: 7]
    i += 1
    
endtime = time.time()

print("time substr used {}".format(endtime-starttime))
