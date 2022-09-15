import cv2 as cv

capture = cv.VideoCapture('E:\\My Mobile Media\\Camera 12_06_22\\VID_20210522_175449.mp4')

while True:
    success, frame = capture.read()

    frame_r = cv.resize(frame, (400, 600))

    frame_r = cv.flip(frame_r, 0)

    gray = cv.cvtColor(frame_r, cv.COLOR_BGR2GRAY)

    harr_cascade = cv.CascadeClassifier('./cascade.xml')

    face_coords = harr_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

    for (x,y,w,h) in face_coords:
        cv.rectangle(frame_r, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

    cv.imshow('Video', frame_r)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()