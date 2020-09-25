import cv2 as cv
import numpy as np
from matplotlib.colors import hsv_to_rgb


img = cv.imread('tomatoes_and_apples.jpg')
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_purple = np.array([(20, 100, 20)])
upper_purple = np.array([(40,255,255)])
img_hsv = cv.GaussianBlur(img_hsv, (3, 3), 0)
img_hsv = cv.inRange(img_hsv, lower_purple, upper_purple)

kernel = np.ones((7, 7), np.uint8)
img_hsv = cv.dilate(img_hsv, kernel)

contours, hierarchy = cv.findContours(img_hsv, 2, 1)
cnt = contours
big_contour = []
max = 0
for i in cnt:
    area = cv.contourArea(i)  # --- find the contour having biggest area ---
    if (area > max):
        max = area
        big_contour = i

cv.drawContours(img, cnt, -1, (0, 255, 0), -1)



cv.imshow('Korona', img)
cv.imshow('HSV', img_hsv)
cv.waitKey(0)