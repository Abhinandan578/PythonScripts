from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import cv2
import imutils
import time
import dlib
import speech_recognition as sr
# import pyttsx
import os
from gtts import gTTS
import re
def isMatch(str):
	patAcc = ["turn it off","yes"]
	patRej = ["no","don\'t"]
	cntAcc=0
	cntRej=0

	for pat in patAcc:
		if re.search(pat,str):
			cntAcc=cntAcc+1
	for pat in patRej:
		if re.search(pat,str):
			cntRej=cntRej+1
	if cntRej==0 and (cntAcc>=1):
		return True
	elif (cntRej>=1) or cntAcc==0:
		return False

def SLARM():
	# engine = pyttsx.init()
	r = sr.Recognizer()
	with sr.Microphone() as source:
		# engine.say('Hey Abhinandan Shall i turn it off or not')
		tts= gTTS(text="Hey Abhinandan shall i turn it off or not",lang="en")
		# engine.runAndWait()
		tts.save("/pythonScripts/SleepDetector/hello.mp3")
		os.system('mpg321 /pythonScripts/SleepDetector/hello.mp3')
		audio = r.listen(source)

	try:
		str=r.recognize_google(audio)
		print("You said : " + str)
		if isMatch(str):
			print("True")
			os.system("poweroff")
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		SLARM()
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
		SLARM()

def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1],eye[5])
	B = dist.euclidean(eye[2],eye[4])
	C = dist.euclidean(eye[0],eye[3])
	ear = (A+B)/(2.0*C)
	return ear

EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 35

COUNTER = 0
TOTAL = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/pythonScripts/SleepDetector/shape_predictor_68_face_landmarks.dat")

(lStart,lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart,rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap=cv2.VideoCapture(0)
while True:
	_,image = cap.read()
	image = imutils.resize(image,width=450)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	rects = detector(gray,0)

	for rect in rects:
		shape=predictor(gray,rect)
		shape=face_utils.shape_to_np(shape)
				
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]

		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)

		ear = (leftEAR + rightEAR)/ 2.0

		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)

		cv2.drawContours(image,[leftEyeHull],-1,(0,255,0),1)
		cv2.drawContours(image,[rightEyeHull],-1,(0,255,0),1)

		if ear < EYE_AR_THRESH:
			COUNTER +=1

		else:
			if COUNTER >= EYE_AR_CONSEC_FRAMES:
				cv2.putText(image, "Sleeping",(10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				print("Sleeping")
				SLARM()
				print("Ear is ",ear)

			COUNTER = 0

		# cv2.putText(image, "Blinks: {}".format(TOTAL),(10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		cv2.putText(image, "EAR: {:.2f}".format(ear), (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


	cv2.imshow("Output",image)
	k=cv2.waitKey(5)&0xFF
	if k==ord('q'):
		break


cv2.destroyAllWindows()
cap.release()