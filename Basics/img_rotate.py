import cv2 as cv

img = cv.imread('E:\My Mobile Media\Pen Drive 1\Pokemon GO\IMG-20170302-WA0109.jpg')

# cv.imshow('Base Image', img)

def rescaleImage(img, scale = 0.5):
    width = int(img.shape[1] * scale)     # [1] -> width
    height = int(img.shape[0] * scale)    # [0] -> height

    dimensions = (width,height)

    return cv.resize(img, dimensions, interpolation = cv.INTER_AREA)

img2 = rescaleImage(img)
# cv.imshow('Image', img2)

def rotateImage(img, angle, rotPt = None):
    (height, width) = img.shape[:2]

    if rotPt is None:
        rotPt = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPt, angle, 1.0)
    
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotateImage(img2, 180)
# rotated = rotateImage(img2, 90, (80,80))

cv.imshow('Rotated Image', rotated)

cv.waitKey(0)