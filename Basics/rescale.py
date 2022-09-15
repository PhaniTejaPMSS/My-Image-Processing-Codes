import cv2 as cv

capture = cv.VideoCapture('E:\My Mobile Media\DCIM 06_08_2022\Camera\VID_20220730_180530(0).mp4')

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)     # [1] -> width
    height = int(frame.shape[0] * scale)    # [0] -> height

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

