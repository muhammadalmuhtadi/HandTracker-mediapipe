def handtrack ():
    import cv2
    import mediapipe as mp

    # FPS MODULE
    # import time
    # pTime = 0
    # cTime = 0

    driver = cv2.VideoCapture('test.mp4')

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    

    while True:
        success, img = driver.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                # for id, lm, in enumerate(handLms.landmark): POINTER FOR HAND
                #     h,w,c = img.shape
                #     cx, cy = int(lm.x*w), int(lm.y*h)
                #     print (id, cx, cy)
                #     if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                #         cv2.circle(img, (cx, cy), 10, (255,0,0), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        #buat fps
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0), 3)
        

        cv2.imshow("Image", img)
        cv2.waitKey(1)