
# example taken from: https://docs.opencv.org/4.5.2/d4/dc6/tutorial_py_template_matching.html

import cv2 as cv
import numpy as np
import os


fileNameMain = input("enter your main image")

assert os.path.exists(fileNameMain), "I did not find the file at, "+str(fileNameMain)


fileNameFind = input("enter the image you looking for")

assert os.path.exists(fileNameFind), "I did not find the file at, "+str(fileNameFind)


RED = (0,0,255)
fileNameOut = 'ouput.png'

img_rgb  = cv.imread(fileNameMain)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread(fileNameFind, 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), RED, 2)
cv.imwrite(fileNameOut, img_rgb)
