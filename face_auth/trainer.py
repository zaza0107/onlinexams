import os
import cv2
import numpy as np
from PIL import Image

class Train:

	#get the images from dataset folder and train them
	def getImagesWithID(self,path):
		imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
		faces = []
		IDs = []
		for imagePath in imagePaths:
			faceImg = Image.open(imagePath).convert('L')
			faceNp = np.array(faceImg,'uint8')
			convId = os.path.split(imagePath)[-1].split('.')[1]
			ID = int(''.join(str(ord(c)) for c in convId))
			print ID
			faces.append(faceNp)
			IDs.append(ID)
			cv2.imshow("training",faceNp)
			cv2.waitKey(10)
		return IDs,faces

	# save the trained yml file in recognizer folder
	def saveRec(self):
		IDs,faces = self.getImagesWithID(path)
		recognizer.train(faces,np.array(IDs))
		recognizer.write('recognizer/trainingData.yml')
		cv2.destroyAllWindows()

t = Train()
t.getImagesWithID(path)
t.saveRec()