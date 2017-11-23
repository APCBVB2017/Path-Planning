import cv2
import numpy as np


rows = 17
columns = 17

def grid_map(img):
    # create a 2d array
    cv2.imshow("image.jpg",img)

    grid = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            # white blocks
            if (np.array_equal(img[(i*20), (j*20)], [255, 255, 255])):
                grid[i][j] = 0
            # start -> orange block
            elif (np.array_equal(img[(i*20), (j*20)], [39, 127, 255])):
                grid[i][j] = 2
            # end -> pink block
            elif (np.array_equal(img[(i*20), (j*20)], [201, 174, 255])):
                grid[i][j] = 3
            # obstacles ->black blocks
            else:
                grid[i][j] = 1
    print grid
    return grid
    cv2.waitKey(0)






gray = cv2.imread('Images/test_image6.jpg')
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges-50-150.jpg',edges)
minLineLength=100

lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)


a,b,c = lines.shape
for i in range(a):
    cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1, 4)
    cv2.imwrite('houghlines5.jpg',gray)

grid_map(gray)
