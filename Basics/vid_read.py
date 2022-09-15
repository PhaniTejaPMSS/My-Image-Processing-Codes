import cv2 as cv

# capture = cv.VideoCapture('E:\My Mobile Media\DCIM 06_08_2022\Camera\VID_20220730_180530(0).mp4')
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video Example', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()
