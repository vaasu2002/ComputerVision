import cv2
import mediapipe as mp


mpDraw = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles
mpHands = mp.solutions.hands
hands = mpHands.Hands()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h , w , c = img.shape
                cx, cy =int(lm.x *w) , int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                
            print(lmList)
            mpDraw.draw_landmarks(img, handLms ,mpHands.HAND_CONNECTIONS)  

            if lmList:
                x1, y1 = lmList[4][1] , lmList[4][2]
                x2, y2 = lmList[8][1] , lmList[8][2]
          
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)
