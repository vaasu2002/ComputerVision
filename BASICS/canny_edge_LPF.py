import cv2 as cv2 
img = cv2.imread("image.jpeg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


canny_edge_LPF = cv2.Canny(gray, 25, 25)
cv2.imshow('canny_edge_LPF', canny_edge_LPF)
cv2.waitKey(0)
