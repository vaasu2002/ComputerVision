import cv2 as cv2 
img = cv2.imread("image.jpeg")
b,g,r = cv2.split(img)
cv2.imshow('blue', b)
cv2.imshow('red', r)
cv2.imshow('green', g)
cv2.waitKey(0)
