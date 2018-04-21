import speech_recognition as sr
import pyttsx
import os
def shutdown(self):
    import subprocess
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])

# engine = pyttsx.init()
# r = sr.Recognizer()
# with sr.Microphone() as source:
# 	engine.say('Hey Abhinandan Shall i turn it off or not')
# 	engine.runAndWait()
# 	audio = r.listen(source)
from gtts import gTTS
import os
tts= gTTS(text="Hey Abhinandan Shall i turn it off or not",lang="en")
tts.save("hello.mp3")
os.system('mpg321 hello.mp3')

try:
	str=r.recognize_google(audio)
	print("You said : " + str)
	if str=="turn it off":
		print "True"
		os.system("poweroff")
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
