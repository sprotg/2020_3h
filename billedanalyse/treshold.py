import cv2 #opencv cv: computer vision
import numpy as np

img = cv2.imread('3h.jpg', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

rows, cols = gray.shape

for y in range(rows):
    for x in range(cols):
        if gray[y,x] > 100:
            gray[y,x] = 255
        else:
            gray[y,x] = 0

for y in range(1,cols-1):
    for x in range(1,rows-1):
        sum_r = 0
        sum_g = 0
        sum_b = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                sum_r += gray[x+dx,y+dy]
                #sum_r += gray[x+dx,y+dy,0]
                #sum_g += gray[x+dx,y+dy,1]
                #sum_b += gray[x+dx,y+dy,2]
        blur[x,y] = sum_r/9#(sum_r/9,sum_g/9,sum_b/9)

cv2.imshow("Thresholded image", gray)
cv2.imshow("original", img)
cv2.imshow("blur", blur)
cv2.waitKey(0)
