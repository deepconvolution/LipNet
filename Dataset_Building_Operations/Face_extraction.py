import os
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('color_001.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
import matplotlib.pyplot as plt
faces = face_classifier.detectMultiScale(img,1.3,3)
plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
#cv2.imshow('img',img)
#cv2.waitKey(0)

[[x,y,h,w]] = faces

plt.imshow(img)
#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.imshow('Cropped',img[y:y+h,x:x+w])
#cv2.waitKey(0)
#cv2.destroyAllWindows()
img_crop = img[y:y+h,x:x+w]
plt.imshow(img_crop)
cv2.imwrite('img3.jpg',img_crop)
img_crop = cv2.cvtColor(img_crop, cv2.COLOR_RGB2BGR)
cv2.imwrite('img2.jpg',img_crop)
img2 = cv2.imread('img.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img2)

os.chdir('Dataset')
for f in os.listdir():
    for l in os.listdir():
        for w in os.listdir():
            for p in os.listdir():
                for i in os.listdir():
                    
    