import cv2 as cv

img0 = cv.imread('E:\My Mobile Media\Camera 12_06_22\IMG_20210522_110054.jpg')

img = cv.resize(img0, (600, 500))
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray)

harr_cascade = cv.CascadeClassifier('./harr_cascade.xml')

detected = harr_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 11)     # List

print(f'No. of faces detected : {len(detected)}')

for (x, y, w, h) in detected:
    rect = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)

cv.imshow('Detected Face', rect)

cv.waitKey(0)