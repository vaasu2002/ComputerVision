```ruby
import cv2
import mediapipe as mp
 
capture = cv2.VideoCapture("")
pTime = 0
while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 255, 0), 3)
    cv2.imshow("Video", img)
    cv2.waitKey(1)
    ```
