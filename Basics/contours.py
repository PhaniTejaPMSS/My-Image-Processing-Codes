import cv2 as cv

# Contours = The boundaries of objects, the line or curve that joins the continuous points along the 
#            boundary of an object. They are not Edges in Mathematical point of view!

img = cv.imread('E:\My Mobile Media\Camera 12_06_22\pikachu.jpg', 0)

img2 = cv.resize(img, (400,500))

# Converting into Grayscale, if the image is not read in grayscale mode
# gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

cv.imshow('Image', img2)

# To detect the edges in the image, we use the Canny Edge Detector
canny = cv.Canny(img2, 30, 200)    
# The more the numbers (ex: 180, 180), the most bright edges will be detected leaving the least bright ones.

cv.imshow('Canny Image', canny)

# Finding Contours
contours, heirarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

cv.imshow('Contours', canny)

print('No. of contours found: ' + str(len(contours)))



cv.waitKey(0)