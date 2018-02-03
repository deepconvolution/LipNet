#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:53:41 2018

@author: saquib
"""

import os
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('photos.png')
faces = face_classifier.detectMultiScale(img,1.3,2)

os.chdir('Dataset')
for f in os.listdir():
    os.chdir(f)
    for l in os.listdir():
        os.chdir(l)
        for w in os.listdir():
            os.chdir(w)
            for p in os.listdir():
                os.chdir(p)
                if os.path.exists('Testing') == False:
                    os.mkdir('Testing')
                for i in os.listdir():
                    if os.path.isdir(i) == False:
                        img = cv2.imread(i)
                        faces = face_classifier.detectMultiScale(img,1.3,2)
                        if faces is not ():
                            for (x,y,h,w) in faces:
                                name = 'Testing/cropped_'+i
                                cv2.imwrite(name,img[y:y+h,x:x+w])
                os.chdir('..')
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')

