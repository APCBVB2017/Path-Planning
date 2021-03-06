import cv2
import numpy as np

img = cv2.imread('Images/test_image6.jpg', 0)

_, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

mask = np.ones_like(img) * 255
boxes = []

for contour in contours:
    if cv2.contourArea(contour) > 100:
        hull = cv2.convexHull(contour)
        cv2.drawContours(mask, [hull], -1, 0, -1)
        x,y,w,h = cv2.boundingRect(contour)
        boxes.append((x,y,w,h))

boxes = sorted(boxes, key=lambda box: box[0])

mask = cv2.dilate(mask, np.ones((5,5),np.uint8))

img[mask != 0] = 255

result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

for n,box in enumerate(boxes):
    x,y,w,h = box
    cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(result, str(n),(x+5,y+17), cv2.FONT_HERSHEY_SIMPLEX, 0.2,(255,0,0),1,cv2.LINE_AA)

cv2.imwrite('result.png', result)
