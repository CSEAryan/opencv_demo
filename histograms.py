#it allows you to visualize the intesity of pixel
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"C:\Users\Aryan Thapa\Desktop\aryan.jpg")
cv.imshow("Mine", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

#circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

#masked = cv.bitwise_and(gray, gray, mask=circle)
#cv.imshow("masked", masked)
#grayscale histogram
#histogram without applying mask
#gray_hist =cv.calHist([gray],[0],None, [256],[0,256])
#gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256])

#plt.figure()
#plt.title('GrayScale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#color Histogram
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("masked", masked)
#without masking
#color_hist = cv.calcHist([img], [0], None, [256], [0,256])
#plt.figure()
#plt.title('ColoredImg Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')

#colors =('b','g','r')
# with masking None will be replaced with masked
#for i,col in enumerate(colors):
#    hist = cv.calcHist([img],[i], None,[256],[0,256])
#    plt.plot(hist, color = col)
#    plt.xlim([0,256])


#plt.show()


#using masking for colored image histogram
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)
plt.figure()
plt.title('ColoredImg Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors =('b','g','r')
# with masking None will be replaced with masked
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], mask,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])


plt.show()





cv.waitKey(0)
