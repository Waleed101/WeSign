import cv2
dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\\"
video = cv2.VideoCapture(dir_path + "our_approach.mp4")

while True: 
  
    # extracting the frames 
    ret, img = video.read() 
      
    # converting to gray-scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # displaying the video 
    cv2.imshow("Live", gray) 
  
    # exiting the loop 
    key = cv2.waitKey(1) 
    if key == ord("q"): 
        break
      
# closing the window 
cv2.destroyAllWindows() 
video.release()