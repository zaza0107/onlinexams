import os
import cv2
import numpy as np

class User:
	def __init__( self,id):
		self.id = id

	#create dataset of user faces and save it in dataset folder
	def save(self):
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		cap = cv2.VideoCapture(0)
		sampleNumber = 0
		while True:
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(gray,1.3,5)
			for(x,y,w,h) in faces:
				sampleNumber += 1
				cv2.imwrite("dataset/user."+str(id)+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				cv2.waitKey(100)
			cv2.imshow('img',img)
			cv2.waitKey(1)
			if(sampleNumber>20):
				break		
		cap.release()
		cv2.destroyAllWindows()


	ask for username and password and save it in txt file
	def UsernamePassword(self):
		f = open('UserDetails/'+str(''.join(str(ord(c)) for c in id))+'.txt','w')
		a = input('Username ')
		b = input('Password ')
		f.write(str(a)+'#'+str(b))
		f.close()
enter numbers
id = input('enter user id ')
u1 = User(id)
u1.save()
u1.UsernamePassword()