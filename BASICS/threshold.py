import cv2 as cv2 
img = cv2.imread("image.jpeg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
