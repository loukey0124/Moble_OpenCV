# 0202.py
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) 
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

#=================================

imgFile1 = './data/Lena.bmp'
imgFile2 = './data/Lena2.jpg'

img1 = cv2.imread(imgFile1)
img2 = cv2.imread(imgFile2)

cv2.imshow("Lena.bmp", img1)
cv2.imshow("Lena2", img2)

cv2.waitKey()
cv2.destroyAllWindows()