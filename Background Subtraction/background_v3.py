import cv2
cap=cv2.VideoCapture(1)
j=0
while 1:
    ret,frame=cap.read()
    if(j==0):
        bg=frame.copy().astype("float")
    if(j<30):
        cv2.accumulateWeighted(frame,bg,0.5)
        j=j+1
    diff=cv2.absdiff(frame,bg.astype("uint8"))
    diff=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    thre,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    cv2.imshow("j",diff)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()