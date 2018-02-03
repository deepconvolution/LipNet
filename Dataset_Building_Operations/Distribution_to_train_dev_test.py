#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 03:34:16 2018

@author: saquib
"""

import os
import numpy as np
import cv2

str = 'F01_phrases01_01.jpg'

fn,ext = os.path.splitext(str) 
f1,f2,f3 = fn.split('_')

idx = f2[-2:]
i = 0 
if idx[0]==0:
    i = int(idx[1]) - 1
else:
    i = int(idx) - 1
if f2[:-2] == 'phrases':
    i = i
else:
    i = i + 10
print(f2[:-2])
os.chdir('Dataset2')
for f in os.listdir():
    if os.path.isdir(f) == False:
        fn,ext = os.path.splitext(f) 
        f1,f2,f3 = fn.split('_')
        idx = f2[-2:]
        i = 0 
        if idx[0]==0:
            i = int(idx[1]) - 1
        else:
            i = int(idx) - 1
        if f2[:-2] != 'phrases':
            i = i + 10
        dirt = str(i)
        if os.path.exists(dirt) == False:
            os.mkdir(dirt)
        name = dirt+'/'+f
        os.rename(f,name)
