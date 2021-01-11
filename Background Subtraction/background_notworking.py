import cv2 as cv
import numpy as np

img_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\b.jpg"
img = cv.imread(img_path)

hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV, (2,2))
ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
cv.imshow("thresh", thresh)
cv.waitKey(0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = max(contours, key=lambda x: cv.contourArea(x))
cv.drawContours(img, [contours], -1, (255,255,0), 2)
img_gray = cv.cvtColor(img, cv.COLOR_HSV2GRAY)
cv.imshow("contours", img_gray)
cv.waitKey(0)