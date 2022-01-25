import cv2 as cv2 
img = cv2.imread("image.jpeg")
b,g,r = cv2.split(img)
merge = cv2.merge([b,g,r])
cv2.imshow('merged', merge)
cv2.waitKey(0)
