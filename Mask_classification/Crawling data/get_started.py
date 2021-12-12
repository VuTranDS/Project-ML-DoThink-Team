from os import listdir
from os.path import isfile, join
from extract_img import faces
import cv2
import dlib
from os import listdir
from os.path import isfile, join


def detect_face():
	mypath = "datasets/"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for file in onlyfiles:
		img = cv2.imread(mypath+file)
		faces(img)
		# print(img)
		# print(file)
detect_face()