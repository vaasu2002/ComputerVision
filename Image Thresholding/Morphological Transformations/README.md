# Morphological Transformations
![Original Images](https://github.com/vaasu2002/ComputerVision/blob/main/Image%20Thresholding/Morphological%20Transformations/IMAGES/original.png)

### Dilation
Add pixel to the boundart, connects area that are seperated, in gray scale image dialation increases the brightness of the object,
```ruby
import cv2
import numpy as np

img = cv2.imread('img/op.png',0) # GRAY SCALE
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow('Dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
