
dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\\"

import cv2
img = cv2.imread(dir_path + 'b.jpg') # load a dummy image
while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print(k) # else print its value