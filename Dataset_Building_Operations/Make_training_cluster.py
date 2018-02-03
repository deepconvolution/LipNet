#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:29:49 2018

@author: saquib
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
tdir = '/home/saquib/Downloads/LipNet/Dataset/'
os.chdir('Dataset')
for f in os.listdir():
    os.chdir(f)
    for l in os.listdir():
        os.chdir(l)
        for w in os.listdir():
            os.chdir(w)
            for p in os.listdir():
                os.chdir(p)
                os.chdir('lip_Testing')
                seq = np.zeros((224,224))
                orig = len(os.listdir())
                orig_image = []
                for i in os.listdir():
                    img = cv2.imread(i,0)
                    img = cv2.resize(img,(32,32),interpolation = cv2.INTER_LINEAR)
                    orig_image.append(img)
                x_limit = 32
                y_limit = 32
                iterator_x = 0
                iterator_y = 0
                for i in range(0,49):
                	#seq[iterator_x:iterator_x+x_limit,iterator_y:iterator_y+y_limit] = orig_image[int((i*orig)/49)] movement along x-axis
                    seq[iterator_y:iterator_y+y_limit,iterator_x:iterator_x+x_limit] = orig_image[int((i*orig)/49)] # movement along y-axis
                    iterator_x = iterator_x + x_limit
                    if iterator_x == 224:
                        iterator_x = 0 
                        iterator_y = iterator_y + y_limit 
                name = tdir+f+'_'+l+w+'_'+p+'.jpg'
                cv2.imwrite(name,seq)
                os.chdir('..')
                os.chdir('..')
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')
    
