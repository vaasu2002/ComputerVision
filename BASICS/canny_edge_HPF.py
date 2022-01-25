import cv2 as cv2 
img = cv2.imread("image.jpeg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


canny_edge_HPF = cv2.Canny(gray, 255, 255)
cv2.imshow('canny_edge_HPF', canny_edge_HPF)
cv2.waitKey(0)
