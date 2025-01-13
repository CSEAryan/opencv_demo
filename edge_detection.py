import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
cv.imshow("Mine", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed", gray)

#laplaction
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#sabel
#gradient to direction

sobelx  = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow("Combined",combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)