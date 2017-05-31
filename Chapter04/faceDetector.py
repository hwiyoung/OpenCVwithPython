import cv2
import numpy as np

#face_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('C:/Users/Hwiyoung/Anaconda3/pkgs/opencv-3.2.0-np111py36_201/Library/etc/haarcascades/haarcascade_frontalface_default.xml')

'''
# in case of Video
cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while True:
	ret, frame = cap.read()
	frame = cv2.resize(frame, Non, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in face_rects:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
	
	cv2.imshow('Face Detector', frame)
	
	c = cv2.waitKey(1)
	if c == 27:
		break
		
cap.release()
cv2.destoryAllWindows()
'''

# in case of Image
img = cv2.imread('./images/IMG.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_rects = face_cascade.detectMultiScale(gray, 1.3, 5) # img, scaling_factor, threshold
for (x,y,w,h) in face_rects:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

cv2.imshow('Face Detector', img)
c = cv2.waitKey()