import cv2
import numpy as np


# rows = 10
# columns = 10
#
# def grid_map(img):
#     # create a 2d array
#     grid = np.zeros((rows, columns))
#     for i in range(rows):
#         for j in range(columns):
#             # white blocks
#             if (np.array_equal(img[20+(i*40), 20+(j*40)], [255, 255, 255])):
#                 grid[i][j] = 0
#             # start -> orange block
#             elif (np.array_equal(img[20+(i*40), 20+(j*40)], [39, 127, 255])):
#                 grid[i][j] = 2
#             # end -> pink block
#             elif (np.array_equal(img[20+(i*40), 20+(j*40)], [201, 174, 255])):
#                 grid[i][j] = 3
#             # obstacles ->black blocks
#             else:
#                 grid[i][j] = 1
#     print grid
#     return grid





gray = cv2.imread('SampleImages/test_image6.jpg')
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imwrite('edges-50-150.jpg',edges)
minLineLength=100
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

a,b,c = lines.shape
for i in range(a):
    cv2.line(gray, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imwrite('houghlines5.jpg',gray)
