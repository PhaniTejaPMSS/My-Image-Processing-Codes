import cv2 as cv

img0 = cv.imread('E:\My Mobile Media\Camera 12_06_22\IMG_20210203_170405.jpg')

img = cv.resize(img0, (400, 540))

cv.imshow('Image', img)

# Color to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale', gray)

# Grayscale to HSV      (HSV = Hue, Saturation, Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('HSV Image', hsv)

cv.waitKey(0)