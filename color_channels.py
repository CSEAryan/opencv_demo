import cv2 as cv
import numpy as np

#opencv allows us to split the images into three color channels blur green and red

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow("Mine",img)

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow("Green", g)
cv.imshow("Red", r)

#printing the shape of the image and the color channels
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)

cv.waitKey(0)