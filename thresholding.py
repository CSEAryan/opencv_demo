import cv2 as cv

#thresholding helps to binarize the image

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
cv.imshow("Mine", img)


#converting bgr image to gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayed", gray)

#Simple Thresholding
# 150 vanda small vaye 0 set gardinca navaye 255 set gardinxa pixel value lai
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded", thresh)
#Inversema 150 vanda small vaye 255 gardinca navye 0 set gardinxa so we will get inverse output
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded Inverse", thresh_inv)
#Adaptive Threshold
#computer will decide the optimal threshold value on basis of mean, gaussian, etc
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,                                      11,3)
cv.imshow("Adaptive Thresholding", adaptive_thresh)
#for fine tuning
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV,
                                       11,3)
cv.imshow("Adaptive Thresholding Inverse", adaptive_thresh_inv)


cv.waitKey(0)