import os
import cv2
import numpy as np


os.chdir('Dataset')
for f in os.listdir():
    os.chdir(f)
    for l in os.listdir():
        os.chdir(l)
        for w in os.listdir():
            os.chdir(w)
            for p in os.listdir():
                os.chdir(p)
                for i in os.listdir():
                    if os.path.isdir(i) == False:
                        os.remove(i)
                os.chdir('..')
                print('Cleaned :',p)
            os.chdir('..')
        os.chdir('..')
    os.chdir('..')


