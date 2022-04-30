import cv2
import mediapipe as mp
import time
import keyboard

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTIme = 0

run = True

while run:
    success, img = cap.read()
    # convert to rgb as the mpHands.Hands() uses rgb
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # calculating FPS
    cTIme = time.time()
    fps = 1 / (cTIme - pTime)
    pTime = cTIme

    # Shows FPS
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # press enter to terminate program
    if keyboard.is_pressed('enter'):
        break