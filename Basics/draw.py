import cv2 as cv
import numpy as np

blank = np.zeros((600,600,3), dtype = 'uint8')      # Here, "uint8" is the datatype of an image
# In the above dimensions, first is width, second is height and third is color code(ex: 0,255,0 = red)

# cv.imshow('Base Image', blank)

# Painting the image

# Number 1 (Small Blocks)
# blank[:] = 0,255,4
# blank[50:150, 250:350] = 0,0,255
# blank[0:40, 250:500] = 0,255,0

# Number 2 (Rectangle)
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 10)      # Just the outline
# cv.rectangle(blank, (0,0), (250,300), (0,255,0), thickness = -1)        # Fills the color 

# Number 3 (Circle)
# cv.circle(blank, (300,350), 50, (0,255,0), thickness = 5)
# cv.circle(blank, (blank.shape[1]//3, blank.shape[0]//4), 40, (255,0,0), thickness = -1)

# Number 4 (Line)
cv.line(blank, (30,30), (550,550), (255,0,0), thickness = 2)

cv.imshow('Painted Image', blank)

cv.waitKey(0)