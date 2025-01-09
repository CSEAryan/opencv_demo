import cv2 as cv

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")

cv.imshow('mine', img)

#converting to greyscale

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grey', gray)

#bluring the image
# to increase the blur amount we can simply increase the ksize
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edgecascade
#helps to find the edges on the image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

#how to dilate the image
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow('Eroded', eroded)


#Resize image

#resized = cv.resize(img, (500,500))
#Interpolation is necessary when we are shrinking the images from original size
# and if we are expanding the images then we use  cv.INTER_LINEAR as interpolation value
# or we will use INTER_CUBIC
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('resized', resized)

#Cropping the images
cropped = img[400:500, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)
