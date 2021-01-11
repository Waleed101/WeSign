dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\white.mp4"

import cv2

vcap = cv2.VideoCapture(dir_path) # 0=camera
 
if vcap.isOpened(): 
    width  = vcap.get(3) # float
    height = vcap.get(4) # float

print(width)
print(height)