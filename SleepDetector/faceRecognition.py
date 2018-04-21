import cv2
import numpy as np
import os

subjects = ["","Abhinandan"]

def detect_face(img):
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face_cascade=cv2.CascadeClassifier('lbpcascade_frontalface.xml')

	faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5);
	if(len(faces)==0):
		return None,None
	(x,y,w,h) = faces[0]

	return gray[y:y+w,x:x+h],faces[0]
def prepare_training_data(data_folder_path):
	dirs = os.listdir(data_folder_path)	
	faces=[]
	labels=[]
	for dir_name in dirs:
		if not dir_name.startswith("s"):
			continue;
		label = int(dir_name.replace("s",""))
		subject_dir_path = data_folder_path + "/"+ dir_name
		subject_images_names = os.listdir(subject_dir_path)
		for image_name in subject_images_names:
			if image_name.startswith("."):
				continue;
			image_path = subject_dir_path + "/" + image_name
			image= cv2.imread(image_path)
			cv2.imshow("Training on image..",image)
			cv2.waitKey(1)
			face,rect = detect_face(image)

			if face is not None:
				print("Hello")
				print(image_name)
				faces.append(face)
				labels.append(label)
			cv2.destroyAllWindows()
		cv2.waitKey(1)
		cv2.destroyAllWindows()
	return faces,labels	

print("Printing data...")
faces,labels = prepare_training_data("training-data")
print("Data prepared")

print("Total faces: ",len(faces))
print(labels)
print("Total labels: ",len(labels))

# face_recognizer = cv2.face.createLBPHFaceRecognizer() 
face_recognizer = cv2.face.LBPHFaceRecognizer_Create()
face_recognizer.train(faces,np.array(labels))

def draw_rectangle(img,key):
	(x,y,w,h) = rect
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

def draw_text(img,text,x,y):
	cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)

def predict(test_img):
	img=test_img.copy()
	face,rect = detect_face(img)
	label=face_recognizer.predict(face)
	label_text = subjects[label]
	draw_rectangle(img,rect)
	draw_text(img,label_text,rect[0],rect[1]-5)
	return img

cap=cv2.VideoCapture(0)
while True:
	_,image = cap.read()
	predicted_img=predict(image)
	print("Prediction Complete")
	cv2.imshow(subjects[1],predicted_img)
	k=cv2.waitKey(5)&0xFF
	if k==ord('q'):
		break


cv2.destroyAllWindows()
cap.release()

