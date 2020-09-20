import cv2 as cv
import numpy as np
import pyautogui as pya

#haystack
diablo_window = cv.imread("Testpic.PNG", cv.IMREAD_UNCHANGED)
#needle
trigger_img = cv.imread("Rat1.png",cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(diablo_window, trigger_img, cv.TM_CCOEFF_NORMED)

#get best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print("Best match top left pos: %s" % str(max_loc))
print("Best match confidence: %s" % max_val)

#check values if there is a match
threshold = 0.3
if max_val >= threshold:
    print("Trigger found")

    #get dimension of trigger image
    trigger_w = trigger_img.shape[1]
    trigger_h = trigger_img.shape[0]

    top_left = max_loc
    bottom_right =  (top_left[0]+ trigger_w, top_left[1] + trigger_h)

    cv.rectangle(diablo_window, top_left, bottom_right, color=(0, 255, 0), thickness = 2, lineType=cv.LINE_4)

    
    cv.imshow("Result", diablo_window)
    cv.waitKey()
    #cv.imwrite("result.jpg", diablo_window)

else:
    print("Nothing found")