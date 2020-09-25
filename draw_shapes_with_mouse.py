import numpy as np
import cv2 as cv
drawing = False
circle = False;# true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
number = 0
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode, number
    if event == cv.EVENT_LBUTTONDOWN:
        number += 1
        string = str(number)
        cv.rectangle(img, (2 * x, 2 * y), (x, y), (0, 255, 0), 2)
        cv.putText(img, string, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        number += 1
        string = str(number)
        cv.circle(img, (x, y), 50, (255, 0, 0), 2)
        cv.putText(img, string, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

img = np.zeros((512,512,3), np.uint8)


cv.namedWindow('image')
cv.setMouseCallback('image',draw)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()