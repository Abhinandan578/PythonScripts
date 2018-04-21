from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import cv2
import imutils
import time
import dlib
import speech_recognition as sr
import pyttsx
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
	# sound = engine.getProperty('voices')
	# engine.setProperty('voice',sound[29].id)
	# print(engine.getProperty('voice'))
	# engine.say('Thanks for subscribing me')
	# engine.runAndWait()
	os.system("espeak 'The quick brown fox'")
	# r = sr.Recognizer()
	# with sr.Microphone() as source:
	# engine.say('Hey Abhinandan Shall i turn it off or not')
		# tts= gTTS(text="Hey Abhinandan shall i turn it off or not",lang="en")
	# voices = engine.getProperty('voices')
	# for voice in voices:
 #   		engine.setProperty('voice', voice.id)
 #   		engine.say('The quick brown fox jumped over the lazy dog.')
 #   		engine.runAndWait()
	# print("Rate is ",engine.getProperty('rate'))
	# print("Voice is ",engine.getProperty('voice'))
	# print("Volume is",engine.getProperty('volume'))
		# tts.save("hello.mp3")
		# os.system('mpg321 hello.mp3')
	# 	audio = r.listen(source)

	# try:
	# 	str=r.recognize_google(audio)
	# 	print("You said : " + str)
	# 	if isMatch(str):
	# 		print("True")
	# 		# os.system("poweroff")
	# except sr.UnknownValueError:
	# 	print("Google Speech Recognition could not understand audio")
	# 	SLARM()
	# except sr.RequestError as e:
	# 	print("Could not request results from Google Speech Recognition service; {0}".format(e))
	# 	SLARM()

SLARM()