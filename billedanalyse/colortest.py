import cv2 #opencv cv: computer vision
import numpy as np

img = cv2.imread('colortest.png', cv2.IMREAD_UNCHANGED)
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rows, cols, ch = imghsv.shape

print(imghsv[0,0])
print(imghsv[499,0])
print(imghsv[0,499])
print(imghsv[499,499])

lower_blue = np.array([175,0,0])
upper_blue = np.array([178,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(imghsv, lower_blue, upper_blue)

cv2.imshow("original", img)
cv2.imshow("blå pixels", mask)
cv2.waitKey(0)


# Bitwise-AND mask and original image
#res = cv2.bitwise_and(imghsv,imghsv, mask= mask)
