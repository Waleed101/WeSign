dir_path = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\\"
word_freq = r"C:\Users\walee\Desktop\Clubs\Competitions\2021 WEC\word-frequency.txt"

import cv2
import numpy as np
import sys
from math import log
# import pyttsx3

# # initialize engine
# engine = pyttsx3.init()

# # set properties
# engine.setProperty('rate', 150) # speed percent
# engine.setProperty('volume', 0.9) # Volume 0-1

# # Text-to-speech function
# def speak(s):
#     engine.say(s)
#     engine.runAndWait()

BACKGROUND_VIDEO_HEIGHT = 360
BACKGROUND_VIDEO_WIDTH = 640
hand_image = cv2.imread(dir_path + "hand.png")
hand_trans = cv2.imread(dir_path + "hand_trans.png");

# # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
# words = open(word_freq).read().split()
# wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
# maxword = max(len(x) for x in words)

# def stringToWords(s):
#     s = s.lower()
#     # dynamic programming to infer location of spaces in string

#     # find best match, given for i characters given i-1 cost
#     # returns a pair (match_cost, match_length).
#     def best_match(i):
#         candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
#         return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

#     # build the cost array.
#     cost = [0]
#     for i in range(1,len(s)+1):
#         c,k = best_match(i)
#         cost.append(c)

#     # backtrack to recover the minimal-cost string.
#     out = []
#     i = len(s)
#     while i>0:
#         c,k = best_match(i)
#         assert c == cost[i]
#         out.append(s[i-k:i])
#         i -= k

#     return " ".join(reversed(out))

# def stringToSpeech(s):
#     sentence = stringToWords(s)
#     speak(sentence)

def merge_image(back, front, x,y):
        # convert to rgba
        if back.shape[2] == 3:
                back = cv2.cvtColor(back, cv2.COLOR_BGR2BGRA)
        if front.shape[2] == 3:
                front = cv2.cvtColor(front, cv2.COLOR_BGR2BGRA)

        # crop the overlay from both images
        bh,bw = back.shape[:2]
        fh,fw = front.shape[:2]
        x1, x2 = max(x, 0), min(x+fw, bw)
        y1, y2 = max(y, 0), min(y+fh, bh)
        front_cropped = front[y1-y:y2-y, x1-x:x2-x]
        back_cropped = back[y1:y2, x1:x2]

        alpha_front = front_cropped[:,:,3:4] / 255
        alpha_back = back_cropped[:,:,3:4] / 255
        alpha_front = alpha_front / 1.5

        # replace an area in result with overlay
        result = back.copy()
        result[y1:y2, x1:x2, :3] = alpha_front * front_cropped[:,:,:3] + alpha_back * back_cropped[:,:,:3]
        result[y1:y2, x1:x2, 3:4] = (alpha_front + alpha_back) / (1 + alpha_front*alpha_back) * 255

        return result

def resize(dst,img):
        width = img.shape[1]
        height = img.shape[0]
        dim = (width, height)
        resized = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)
        return resized

print(dir_path + "test_asl.mp4")
video = cv2.VideoCapture(dir_path + "cropped_video.mp4")
# print(video.get(3))
oceanVideo = cv2.VideoCapture(dir_path + "white.mp4")
print(oceanVideo.get(3))
print(oceanVideo.get(4))
success, ref_img = video.read()
ref_img = cv2.imread(dir_path + "newbg.JPG")
print(ref_img.shape)
# print(ref_img.shape)
# ref_img = cv2.imread(dir_path + "background.jpg")
# print(ref_img.shape)
flag = 0
handInPlace = False;
# print(stringToWords("HELLOTHEREISAPERSON"))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('filter_background.avi', fourcc, 20.0, (int(video.get(3)),int(video.get(4))))
while(1):
        success, img = video.read()
        success2, bg = oceanVideo.read()
        bg = resize(bg,ref_img)
        if flag==1:
                ref_img = cv2.imread(dir_path + "newbg.JPG");
                flag = 0
        # create a mask
        diff1=cv2.subtract(img,ref_img)
        diff2=cv2.subtract(ref_img,img)
        diff = diff1+diff2
        diff[abs(diff)<13.0]=0
        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) < 10] = 0
        fgmask = gray.astype(np.uint8)
        fgmask[fgmask>0]=255
        #invert the maskdq
        fgmask_inv = cv2.bitwise_not(fgmask)
        #use the masks to extract the relevant parts from FG and BG
        fgimg = cv2.bitwise_and(img,img,mask = fgmask)
        bgimg = cv2.bitwise_and(bg,bg,mask = fgmask_inv)
        #combine both the BG and the FG images
        dst = cv2.add(bgimg,fgimg)
        # dst = cv2.rectangle(dst, (20, 80), (200, 280), (0, 0, 0), 2) 
        
        # # Top Shape
        # pts = np.array([[20, 80], [35, 105],[185, 105], [200, 80]], np.int32);
        # dst = cv2.fillPoly(dst, [pts], (255, 255, 255))
        # dst = cv2.polylines(dst, [pts], True, (0, 0, 0), 2)

        # dst = cv2.putText(dst, "ASL ROCKS", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2, cv2.LINE_AA);
        # dst = cv2.rectangle(dst, (170, 240), (200, 270), (255, 255, 255), -1) 
        # dst = cv2.rectangle(dst, (170, 240), (200, 270), (0, 0, 0), 2) 
        # dst = cv2.rectangle(dst, (20, 280), (200, 330), (255, 255, 255), -1) 
        # dst = cv2.rectangle(dst, (20, 280), (200, 330), (0, 0, 0), 2) 
        # dst = cv2.rectangle(dst, (20, 330), (200, 400), (255, 255, 255), -1) 
        # dst = cv2.rectangle(dst, (20, 330), (200, 400), (0, 0, 0), 2) 
        # if(handInPlace):
        #         dst = merge_image(dst, hand_image, 175, 243)
        # else:
        #         dst = merge_image(dst, hand_trans, 175, 243)
        # dst = cv2.putText(dst, "A", (105, 305), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 2, cv2.LINE_AA)
        # dst = cv2.putText(dst, "Current", (85, 320), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 0), 2, cv2.LINE_AA)
        # dst = cv2.putText(dst, "HE", (95, 370), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
        # dst = cv2.putText(dst, "Word", (85, 390), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Background Removal',dst)
        out.write(dst)

        key = cv2.waitKey(5) & 0xFF
        if ord('q') == key:
                break
        elif ord('d') == key:
                flag = 1
                print("Background Captured")
        elif ord('r') == key:
                flag = 0
                print("Ready to Capture new Background")
        elif ord('s') == key:
                handInPlace = not handInPlace
                
cv2.destroyAllWindows()
video.release()