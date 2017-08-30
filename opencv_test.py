import cv2
import numpy as np
import datetime,time
#import matplotlib.pyplot as plt

from identifyFace import identifyFace
from detectFace import detectFace

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

setPrintFlag = 0


while (cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_list = []
    cv2.imshow('img',img)
    if len(faces) >0 and setPrintFlag == 0:
        for (x,y,w,h) in faces:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            crop_img = img[y-40 : y+h+40, x-40 : x + w+40] # Crop from x, y, w, h -> 100, 200, 300, 400
            # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
            cv2.imwrite('01.png',crop_img)
            cv2.imshow("cropped", crop_img)
            ts = time.time()
            print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
            detFac = detectFace()
            faceId = detFac.generateFaceId()
        face_list.append(faceId)
        idFace = identifyFace()
        setPrintFlag= idFace.identifyFaceIds(face_list)


    if  len(faces) == 0:
        setPrintFlag = 0

        #roi_color = img[y:y+h, x:x+w]


    k = cv2.waitKey(3) & 0xff
    if k == 2:
        break
cap.release()
cv2.destroyAllWindows()
