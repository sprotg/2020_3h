import time
import cv2
import numpy as np

class Cam():

	def __init__(self):
		#Åbn forbindelse til kameraet.
		#Hvis du har flere kameraer skal du vælge det rigtig tal i parentesen.
		self.vc = cv2.VideoCapture(0)

		self.threshold_value = 115

		#Kriterier for relevante contours
		self.min_area = 500
		self.max_area = 20000
		self.match_score = 0.1

		self.frame = None
		self.show_image = True
		self.reference = cv2.cvtColor(cv2.imread('reference.png',cv2.IMREAD_COLOR), cv2.COLOR_BGR2GRAY)
		cv2.namedWindow("results")
		if self.vc.isOpened():
			print('Forbindelse til kamera er oprettet.')
			rval, self.frame = self.vc.read()
			cv2.imshow("results", self.frame)

	def update(self, t, m, n, s):
		self.threshold_value = int(t)
		self.min_area = int(m)
		self.max_area = int(n)
		self.match_score = float(s)

	def show(self):
		self.analyze(silent=True)
		cv2.imshow("results", self.frame)

	def analyze(self, silent=False):
		if not silent:
			print('Analyserer billede...')
		if self.vc.isOpened():
			rval, self.frame = self.vc.read()

			src_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
			ret, dst = cv2.threshold(src_gray, self.threshold_value, 255, 0)
			cv2.imwrite("./threshold.jpg", dst)
			contours, hierarchy = cv2.findContours(dst, 1, 2)

			sorted_contours = []

			#Sorter på størrelse:
			for c in contours:
				area = cv2.contourArea(c)
				if self.min_area < area < self.max_area:
					cv2.drawContours(self.frame,c,-1,(255,0,0),3)
					sorted_contours.append(c)

			i = 0

			ret, dst = cv2.threshold(self.reference, self.threshold_value, 255, 0)
			ref_cnt, hierarchy = cv2.findContours(dst, 1, 2)

			for c in sorted_contours:
				rect = cv2.minAreaRect(c)
				boxf = cv2.boxPoints(rect)
				#box = np.int0(boxf)


				M = cv2.moments(c)
				hu = cv2.HuMoments(M)
				cx = M['m10']/M['m00']
				cy = M['m01']/M['m00']

				#Tegner en firkant ved cx,cy
				#Bemærk: y,x ikke x,y
				#self.frame[int(cy)-5:int(cy)+5,int(cx)-5:int(cx)+5] = (0,0,(255/len(sorted_contours))*(i+1))

				i += 1

				#Calculate match score:
				# Metode 1 synes at være den bedste.
				score = cv2.matchShapes(ref_cnt[0], c, 1, 0.0)

				if score < self.match_score:
					if not silent:
						print('Der er fundet et A ved ({:5f},{:5f}), i en vinkel på {:5f} grader. Score: {}'.format(cx,cy, rect[2], score))
					#cv2.drawContours(self.frame,[box],0,(0,0,255),2)
					#Vis text
					#cv2.putText(self.frame, "({},{}), Vinkel: {}".format(int(cx),int(cy), rect[2]), (int(cx), int(cy)), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.5, 2)
					#return cx, cy, rect[2]
			cv2.imwrite("./frame.jpg", self.frame)

			if self.show_image:
				cv2.imshow("results", self.frame)
			if not silent:
				print('Analyse færdig.')
			return cx,cy, rect[2]

if __name__ == "__main__":
	c = Cam()

	while True:
		#cmd = input("Skriv > ")
		time.sleep(0.2)
		cx, cy, v = c.analyze()
