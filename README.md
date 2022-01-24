# Computer Vision Learn
```ruby
import cv2
!pip install mediapipe 
```













```ruby
import cv2
path = 'image_name'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) 

imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
```

imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
(7,7) - kernal size
1 - sigma (higher the value of sigma more the blur)
