import cv2
import numpy as np
import matplotlib.pyplot as plt

from findSimilar import findSimilar

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

setPrintFlag = 0


while (cap.isOpened()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    if len(faces) >0 and setPrintFlag == 0:

        cv2.imwrite('01.png',img)
        setPrintFlag = 1
        findSlr = findSimilar()
        findSlr.findName()


    if  len(faces) == 0:
        setPrintFlag = 0

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
