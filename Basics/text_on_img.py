import cv2 as cv
import numpy as np

blank = np.zeros((600,600,3), dtype = 'uint8')
cv.imshow('Base Image', blank)

# blank = cv.imread("E:\My Mobile Media\Pen Drive 1\Pokemon GO\IMG-20170302-WA0109.jpg")

cv.putText(blank, 'Ganesha', (150,450), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 4.0, (255,0,0), thickness = 2 )
cv.imshow('Image with Text', blank)

cv.waitKey(0)