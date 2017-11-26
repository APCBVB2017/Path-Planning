import cv2
import numpy as np




gray = cv2.imread('SampleImages/test_image6.jpg')
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imwrite('edges-50-150.jpg',edges)
minLineLength=100
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80).tolist()
print lines

# for x1,y1,x2,y2 in lines:
#     for index, (x3,y3,x4,y4) in enumerate(lines):

for line in lines:
 for x1,y1,x2,y2 in line:
     for index, (x3,y3,x4,y4) in enumerate(lines):
        if y1==y2 and y3==y4: # Horizontal Lines
            diff = abs(y1-y3)
        elif x1==x2 and x3==x4: # Vertical Lines
            diff = abs(x1-x3)
        else:
            diff = 0

        if diff < 10 and diff is not 0:
            del lines[index]

gridsize = (len(lines) - 2) / 2
