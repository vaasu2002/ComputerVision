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
- To display we use function `mshow` and in **imshow** we need to define two arguments, *name of window* and *image name*.
