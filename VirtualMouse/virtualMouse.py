import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
import mediapipe as mp
################
wCam, hCam = 1024, 480
#################
cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


# 1. Find the hand landmarks
while True:
    success, img = cap.read()
    img = detector.FindHands(img)
    lmlist, bbox = detector.findPosition(img)


# 2. Get the tip of the index and middle fingers
# 3. Check which fingers are up
# 4. Only index finger: Moving mode
# 5. Convert the coordinates
# 6. Smoothen the values
# 7. Move Mouse
# 8. Both index and middle fingers up: Clicking mode
# 9. Find distance between two fingers
# 10. Click mouse if distance short

# 11. Frame rate
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

# 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)




