import cv2
import numpy as np
import os
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer\\trainingData.yml")
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)

#get the details of identfied user
#def getDetails(id):
#	f = open('UserDetails/'+str(id)+'.txt','r')
#	s = f.readline().split("#")
#	usernamea = s[0]
#	passworda = s[1]
#	browser.get('https://www.facebook.com/')
#	username = browser.find_element_by_name('email')
#	username.send_keys(usernamea)
#	password = browser.find_element_by_name('pass')
#	password.send_keys(passworda)
#	signInButton = browser.find_element_by_id('loginbutton')
#	signInButton.click()
#	f.close()

a = True
while a:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
		
        if (Id):
            getDetails(Id)
            a = False
        cv2.putText(img,str(Id),(x,y+h),fontface,fontscale,fontcolor)
        cv2.waitKey(100)
	#cv2.imshow('img',img)
    cv2.waitKey(1)
    if(cv2.waitKey == 27):
        break
    print(Id)

cap.release()
cv2.destroyAllWindows()