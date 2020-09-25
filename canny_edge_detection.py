import numpy as np
import cv2 as cv
import keyboard

tab = []
img = cv.imread('win.png')
b, g, r = cv.split(img)
def draw(event, x, y, flags, param):
    global tab
    global img
    if event == cv.EVENT_LBUTTONDOWN and len(tab) < 2:
        points = [x, y]
        tab.append(points)
    if len(tab) == 2:
        global g, r, b
        g = cv.Canny(img, 20, 200)
        r = cv.Canny(img, 20, 200)
        b = cv.Canny(img, 20, 200)
        g = g[tab[0][1]:tab[1][1], tab[0][0]:tab[1][0]]
        r = b[tab[0][1]:tab[1][1], tab[0][0]:tab[1][0]]
        b = b[tab[0][1]:tab[1][1], tab[0][0]:tab[1][0]]
        crop = cv.merge((b, g, r))
        img[tab[0][1]:tab[1][1], tab[0][0]:tab[1][0]] = crop
        tab = []
cv.namedWindow('image')
cv.setMouseCallback('image', draw)
while keyboard.is_pressed('q') == 0:
    cv.imshow('image', img)
    cv.waitKey(100)
cv.destroyAllWindows()
