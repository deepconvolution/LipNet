#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:32:03 2018

@author: saquib
"""

# import the necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt
import os
# construct the argument parser and parse the arguments
"""
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
    help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
args = vars(ap.parse_args())
"""
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor(args["shape_predictor"])
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') 

# load the input image, resize it, and convert it to grayscale
image = cv2.imread("depth_002.png")
plt.imshow(image)
image = imutils.resize(image, width=56)
plt.figure()
cv2.imwrite('test.jpg',image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# detect faces in the grayscale image
rects = detector(gray, 1)
for (i,rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    for (name,(i,j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
        clone = image.copy()
        cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
 
        # loop over the subset of facial landmarks, drawing the
        # specific face part
        for (x, y) in shape[i:j]:
            cv2.circle(clone, (x, y), 1, (0, 0, 255), -1)
        (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
        roi = image[y:y + h, x:x + w]
        roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
 
        # show the particular face part
        names1=name+'.jpg'
        cv2.imwrite(names1,roi)
        names = name+str(i)+'.jpg'
        cv2.imwrite(names,clone)
output = face_utils.visualize_facial_landmarks(image, shape)
plt.imshow(output)
cv2.waitKey(0)

os.chdir('Dataset')
for f in os.listdir():
    os.chdir(f)
    for l in os.listdir():
        os.chdir(l)
        for w in os.listdir():
            os.chdir(w)
            for p in os.listdir():
                os.chdir(p)
                if os.path.exists('lip_Testing') == False:
                    os.mkdir('lip_Testing')
                for fname in os.listdir():
                    if os.path.isdir(fname) == False:
                        img = cv2.imread(fname)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        rects = detector(gray, 1)
                        for (i,rect) in enumerate(rects):
                            shape = predictor(gray, rect)
                            shape = face_utils.shape_to_np(shape)
                            for (name,(i,j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                                if name=='mouth':
                                    for (x, y) in shape[i:j]:
                                        (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                                        roi = img[y:y + h, x:x + w]
                                        #roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)
                                        
                                        # show the particular face part
                                        name = 'lip_Testing/cropped_'+fname
                                        cv2.imwrite(name,roi)
                os.chdir('..')
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')

a = 4