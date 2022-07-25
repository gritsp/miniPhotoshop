import cv2
from mini import miniPhotoshop

mini = miniPhotoshop()
img = mini.load('./baboon.jpg')
# img = mini.invert(img)
# img2 = mini.addBrighnessAndContrast(img,10,50)
# print(img.load())
# img = load('./opencv.png')

# img = crop(img,10,10,150,150)

# img = rotate(img,"ccw")
# mini.resize(img,50,200)
# img = flip(img,0)
# save = save(img,'test.jpg')
# mini.calHistogram(img)
# cv2.imshow('img2',img2)
# img = mini.convert2gray(img)
# img = mini.addSultAndPaperNoise(img,0.01)
# img = mini.addGossionNoise(img,0.5)
# img2 = mini.blurmedian(img,5)
# img2 = mini.sharpen(img,10)
# img3 = mini.sharpen(img,-1)

# img = mini.edgeDetect(img,2)
# img2 = mini.load('./opencv.png')
# img = mini.subtract(img,img2)
# img = mini.blend(img,img2,0.5)
# img2 = mini.whiteBalance(img)
# img2 = mini.addHSV(img,10,10,-10)
mini.showHistogramRGB(img)

# cv2.imshow('img2',img2)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
