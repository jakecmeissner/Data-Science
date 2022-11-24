import cv2 
import mediapipe as mp
import time
import pose_module as pm

cap = cv2.VideoCapture('vid3.mp4')
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList[25])
    cv2.circle(img, (lmList[25][1], lmList[25][2]), 15, (255, 0, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 250), 3)
    cv2.imshow('Image', img)

    cv2.waitKey(1)

