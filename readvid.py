import cv2

vid = cv2.VideoCapture('sunset.avi')
if (vid.isOpened()==False):
    print('unable to read video')
else:
   while True:
        status,frame= vid.read()
        cv2.imshow('webcam',frame)
        if cv2.waitKey(4)==32:
            break
    