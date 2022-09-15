import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    harr_cascade = cv.CascadeClassifier('./harr_cascade.xml')

    face_coords = harr_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

    for (x, y, w, h) in face_coords:
        rect = cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), thickness = 2)
    
    cv.imshow('Video', rect)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()