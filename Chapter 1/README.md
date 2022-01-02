# CHAPTER 1
```ruby
import cv2
!pip install mediapipe 
```
-----------------
##  1)  IMPORT IMAGE   
```ruby
img = cv2.imread("images.jpg")   # import image
cv2.imshow("Output",img)         
cv2.waitKey(0)                   # add delay( 0 means infinite delay)
```
- To display we use function `imshow` and in **imshow** we need to define two arguments, *name of window* and *image name*.
-----------------
##  2)  IMPORT VIDEO
- we will use `VideoCapture` to import video. As video is a sequence of images we will need a while loop to go through each frame one by one.
- we will capture our image and our image will be saved in variable **img** and **success** variable will tell if it was done succesfully or not, so *success variable will be boolean.* 
```ruby
cap = cv2.VideoCapture("video.mp4")   
while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break```
