import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while (cap.isOpened()):
	ret,frame = cap.read()
	if ret==True:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		rev=cv2.flip(frame,0)
		out.write(rev)
		cv2.imshow('frame',frame)
		cv2.imshow('gray',gray)
		cv2.imshow('reverse',rev)

		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()