import numpy as np
import cv2

img= cv2.imread('watch.jpeg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(45,45),(255,0,0),15)

cv2.rectangle(img,(45,45),(90,150),(0,0,255),5)
cv2.circle(img,(100,65),55,(0,0,255),1)

pts=np.array([[10,5],[20,30],[70,20],[50,10],[70,70]],np.int32)
# pts=pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True,(0,255,255),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!!',(10,130),font,1,(200,255,2),3,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
