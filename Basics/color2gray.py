import cv2 as cv

img = cv.imread('E:\My Mobile Media\Camera 12_06_22\pikachu.jpg')

cv.imshow('Base Image', img)

# Converting into Grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale Image', gray)

# Reading the image in grayscale 
gray_img = cv.imread('E:\My Mobile Media\Pen Drive 1\Pokemon GO\IMG-20170302-WA0109.jpg', 0)

cv.imshow('Grayscale Image Read', gray_img)


cv.waitKey(0)