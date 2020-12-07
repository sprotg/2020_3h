import cv2 #opencv cv: computer vision
import numpy as np

img = cv2.imread('test1.png', cv2.IMREAD_UNCHANGED)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(imggray,127,255,cv2.THRESH_BINARY)
cnt, hierarchy = cv2.findContours(threshold, 1, 2)

reference = cv2.imread('reference2.png', cv2.IMREAD_UNCHANGED)
imggray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
ref_ret, dst = cv2.threshold(imggray, 127, 255, 0)
ref_cnt, hierarchy = cv2.findContours(dst, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

rows, cols = threshold.shape

match_score = 0.17
i = 0
for c in cnt:
    rect = cv2.minAreaRect(c)
    boxf = cv2.boxPoints(rect)
    box = np.int0(boxf)

    i += 1
    #Calculate match score:
    # Metode 1 synes at være den bedste.
    score = cv2.matchShapes(ref_cnt[0], c, 1, 0.0)

    if score < match_score:
        print('Der er fundet en figur ved ({:5f},{:5f}), i en vinkel på {:5f} grader. Score: {}'.format(boxf[2][0],boxf[2][1], rect[2], score))
        # Vis omrids
        cv2.drawContours(img,[c],0,(0,0,255),2)
        #Vis text på billedet
        cv2.putText(img, "({},{}), Vinkel: {}".format(int(boxf[2][0]),int(boxf[2][1]), rect[2]), (int(boxf[2][0]), int(boxf[2][1])), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.7, 2)

cv2.imshow("original", img)
cv2.waitKey(0)
