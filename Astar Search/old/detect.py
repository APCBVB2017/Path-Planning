
import numpy as np
import cv2



im = cv2.imread('SampleImages/test_image6.jpg')

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

imgSplit = cv2.split(im)
flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU)

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(1,1))
cv2.erode(b,element)

edges = cv2.Canny(b,150,200,3,5)

while(True):

    img = im.copy()

lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80).tolist()

    for x1,y1,x2,y2 in lines:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

    cv2.imshow('houghlines',img)

    if k == 27:
        break

cv2.destroyAllWindows()
