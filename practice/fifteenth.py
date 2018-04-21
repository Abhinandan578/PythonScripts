import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbd = cv2.createBackgroundSubtractorMOG2()

while True:
		ret , frame = cap.read()
		fgmask = fgbd.apply(frame)
		cv2.imshow('original',frame)
		cv2.imshow('fg',fgmask)

		k=cv2.waitKey(30) & 0xFF
		if k==ord('q'):
			break
cap.release()
cv2.destroyAllWindows()
