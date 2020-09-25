import numpy as np
import cv2 as cv

img = cv.imread('kolka.png', 0)
img_color = cv.imread('kolka.png', cv.IMREAD_COLOR)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20, param1=15,param2=60,minRadius=60,maxRadius=280)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    x1 = int(i[0] - (i[2]/2))
    x2 = int(i[0] + (i[2]/2))
    y1 = int(i[1] - (i[2]/2))
    y2 = int(i[1] + (i[2] / 2))
    kwadrat= img_color[y1:y2, x1:x2]
    srednia = cv.mean(kwadrat)
    print(srednia[0])
    if(srednia[0] < 60):
        cv.circle(img_color,(i[0],i[1]),i[2],(0,255,0),2)
    else:
        cv.circle(img_color,(i[0],i[1]),i[2],(0,0,255),2)


cv.imshow('detected circles', img_color)
cv.waitKey(0)
cv.destroyAllWindows()