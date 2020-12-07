import cv2 #opencv cv: computer vision
import numpy as np

img = cv2.imread('test1.png', cv2.IMREAD_UNCHANGED)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(imggray,127,255,cv2.THRESH_BINARY)

rows, cols = threshold.shape

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("fandt {} contours".format(len(contours)))



i = 0
for c in contours:
    i+=1
    M = cv2.moments(c)
    hu = cv2.HuMoments(M)
    cx = M['m10']/M['m00']
    cy = M['m01']/M['m00']
    print("Contour {}: {}. Størrelse: {}. Position: {}".format(i, len(c), M["m00"], (cx,cy)))


# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(img, contours, 1, (0, 255, 0), cv2.FILLED)

cv2.imshow("original", imggray)
cv2.imshow("contours", img)
cv2.waitKey(0)
