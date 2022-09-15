import cv2 as cv

img = cv.imread('E:\My Mobile Media\Pen Drive 1\Pokemon GO\IMG-20170302-WA0109.jpg')

# Resizing an Image
img2 = cv.resize(img, (400,480), interpolation = cv.INTER_CUBIC)
# In the above statement, 'interpolation' is not mandatory! The code will run even if it is absent.

cv.imshow('Resized Image', img2)

# Flipping an Image
img3 = cv.flip(img2, flipCode = -1)

# Flipcode -> 0,1,-1    =>  "0" -> Vertical Flip, "1" -> Horizontal Flip, "-1" -> Both Vertical & Horizontal

cv.imshow('Flipped Image', img3)

# Cropping an Image
img4 = img2[240:380]

cv.imshow('Cropped Image', img4)

cv.waitKey(0)