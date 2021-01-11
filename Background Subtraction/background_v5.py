img_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\a.jpg"
background = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\background.jpg"

import cv2 as cv
import numpy as np
import background-rm

image = cv.imread(img_path)
bg = cv.imread(background)
cv.imshow("Before", image)
data = match_substract(image, bg)

cv.waitKey(0)