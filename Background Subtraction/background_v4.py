img_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\b.jpg"

#importing required libraries
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#reading the image
image = cv.imread(img_path)
#converting image to grayscale format
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("temp", gray)
#apply thresholding
ret,thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#get a kernel
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations = 2)
#extract the background from image
sure_bg = cv.dilate(opening,kernel,iterations = 3)

dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret,sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_bg)

ret,markers = cv.connectedComponents(sure_fg)

markers = markers+1

markers[unknown==255] = 0

markers = cv.watershed(image,markers)
image[markers==-1] = [255,0,0]

cv.imshow("temp", sure_fg)

cv.waitKey(0)