import cv2
import numpy as np
from math import tan, atan2, sqrt, degrees

img = cv2.imread('spr_s.jpg', cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
copy = gray.copy()
rows,cols = gray.shape
whites = []
for i in range(rows):
    for j in range(2,cols):
        k = int(gray[i,j])
        km1 = int(gray[i,j-1])
        if abs(k - km1) > 10:
            copy[i,j] = 255
            whites.append((i,j))
        else:
            copy[i,j] = 0
hough_space = np.zeros((180,881), np.uint8)
#(r,a): distance, angle
#Angle between [0;180]
#distance between [0;distance between origin and pixel]
print(len(whites), hough_space.shape)
print(hough_space[0,0])
for pixel in whites:
    a = degrees(atan2(pixel[1], pixel[0]))
    r = sqrt(pixel[0]**2 + pixel[1]**2)
    hough_space[int(a),int(r)] += 25
rows,cols = hough_space.shape
max = 0
max_x = 0
max_y = 0
for y in range(rows):
    for x in range(cols):
        if hough_space[y,x] > max:
            max = hough_space[y,x]
            max_x = x
            max_y = y
print("Max line found at: {},{}. Value: {}".format(max_x, max_y,max))

a = tan(max_y)
for i in range(-100,100):
    x = max_x + i
    y = max_x + x * a
    print("Red: {},{}".format(y,x))
    try:
        img[int(y),int(x)] = [0,0,255]
    except:
        pass
for x in range(20):
    for y in range(20):
        img[y,x] = [0,0,255]

cv2.imshow("Grayscale image", copy)
cv2.waitKey(0)
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.imshow("Hough space", hough_space)
cv2.waitKey(0)
#cv2.imwrite("spr_s.jpg",resized)
cv2.destroyAllWindows()
