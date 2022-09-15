import cv2 as cv
import numpy as np

img = cv.imread('E:\My Mobile Media\Camera 12_06_22\EuFFVOrXcAQKZ_P.jpeg')

cv.imshow('Original Image', img)

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x = right
# -y = up
#  x = left
#  y = down

translated = translate(img, 100, 100)

cv.imshow('Transformed Image', translated)

cv.waitKey(0)