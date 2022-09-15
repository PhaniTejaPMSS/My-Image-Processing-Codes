import cv2 as cv

img0 = cv.imread('E:\My Mobile Media\Pen Drive 1\Pokemon GO\IMG-20170302-WA0109.jpg')

# Resizing the Image
img = cv.resize(img0, (400, 520))

cv.imshow('Base Image', img)

# Blurred Image
blur = cv.GaussianBlur(img, (175,175), cv.BORDER_DEFAULT)

cv.imshow('Blurred Image', blur)

# Edge Cascade
canny = cv.Canny(img, 150, 150)

cv.imshow('Canny Edges', canny)

# Dilated Image
dilated = cv.dilate(img, (150, 150), iterations = 5)

cv.imshow('Dilated Image', dilated)

# Eroded Image
eroded = cv.erode(img, (150, 150), iterations = 5)

cv.imshow('Eroded Image', eroded)

cv.waitKey(0)