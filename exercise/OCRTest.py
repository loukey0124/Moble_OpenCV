import cv2
import pytesseract
import os
from PIL import Image
print(os.getenv("PATH"))
image = cv2.imread('./data/alphabet.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.bmp".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), lang=None)
os.remove(filename)

print(text)
cv2.imshow("1", image)