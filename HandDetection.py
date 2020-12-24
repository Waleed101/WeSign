import cv2 as cv
import numpy as np

img_path = r"C:\Users\edzur\Downloads\wec\fist2.jpg"
img = cv.imread(img_path)

hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV, (2,2))
ret,thresh = cv.threshold(blurred,127,255,cv.THRESH_BINARY)

cv.imshow('thresh',thresh)
cv.waitKey(0)
