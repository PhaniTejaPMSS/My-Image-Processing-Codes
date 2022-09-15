import cv2 as cv
import numpy as np

# capture = cv.VideoCapture('E:\\Simple\\Image Processing\\Yolo\\1 Minute Video - Doggie.mp4')
# capture = cv.VideoCapture('E:\\Simple\\Image Processing\\Yolo\\Car.mp4')
capture = cv.VideoCapture(0)
# capture = cv.VideoCapture('E:\\My Mobile Media\\DCIM 06_08_2022\\Camera\\VID_20220806_132723.mp4')
whT = 320
confidenceThreshold = 0.5       # 50%
nmsThreshold = 0.2          # The lesser it is, the more accurate box will be drawn

classes = []
classesFile = 'coco.names'

with open(classesFile, 'r') as fp:
    classes = fp.read().split()

# print(classes)
# print(len(classes))

modelConfiguration = 'yolov3.cfg'
modelWeights = 'yolov3.weights'

net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

def findObjects(outputs, frame):
    height, width, channels = frame.shape
    height -= 100
    width -= 100
    bbox = []       # bbox - bounding box 
    classIds = []   
    confs = []      # confidence values

    for output in outputs:
        for detected in output:
            scores = detected[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confidenceThreshold:
                w, h = int(detected[2]*width), int(detected[3]*height)
                x, y = int((detected[0]*width)-width/4), int((detected[1]*height)-height/4)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    # print(len(bbox))

    indices = cv.dnn.NMSBoxes(bbox, confs, confidence, nmsThreshold)
    # print(indices[1])

    for i in indices:
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        # print(box)
        w, h = int(w), int(h)   # if this is not int, the program is giving an error output
        cv.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 2)
        cv.putText(frame, f'{classes[classIds[i]].upper()} {int(confs[i]*100)}%',
                    (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)


while True:
    success, frame = capture.read()

    frame_r = cv.resize(frame, (1000, 800))

    blob = cv.dnn.blobFromImage(frame_r, 1/255, (whT, whT), [0,0,0], 1, crop = False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    # print(layerNames)

    outputLayers = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]
    # print(outputLayers)
    # print(net.getUnconnectedOutLayers())

    outputs = net.forward(outputLayers)
    # print(len(outputs))
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)

    # print(outputs[0][0])

    findObjects(outputs, frame_r)

    cv.imshow('Video Capturing', frame_r)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()