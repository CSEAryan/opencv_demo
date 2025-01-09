import cv2 as cv

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow('Mine', img)

#BGR to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


#BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#from BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

#from bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#similar process we can do but we cannot convert grayscale to hsv so gray->bgr->hsv

cv.waitKey(0)