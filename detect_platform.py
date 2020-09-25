import numpy as np
import cv2 as cv
import keyboard

img = cv.imread('drone_ship.jpg', cv.IMREAD_COLOR)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,250,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

while keyboard.is_pressed('q') == 0:
    cv.imshow('image', img)
    cv.waitKey(100)
cv.destroyAllWindows()



