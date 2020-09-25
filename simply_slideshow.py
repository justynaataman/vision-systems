import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keyboard
from glob import glob

data = []
for fn in glob('*.jpg'):
     im = cv.imread(fn, cv.IMREAD_COLOR)
     data.append(im)

i = 0
lenn = len(data)
lenn = lenn
while True:
     print(i)
     if keyboard.is_pressed('d') and i < lenn:
          i = i +1
     if keyboard.is_pressed('a') and i > 0:
          i = i -1
     if keyboard.is_pressed('q'):
          break
     if i == lenn:
          i = 0
     print(i)
     cv.imshow(str(i), data[i])
     cv.waitKey(0)
     cv.destroyAllWindows()








