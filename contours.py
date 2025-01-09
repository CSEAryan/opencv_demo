import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow('mine', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)
#instead of using canny for edge detection we can use threshold

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
# getting the contoours and hierarchies

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), thickness=2)
cv.imshow('Contourdrawn',blank)
cv.waitKey(0)