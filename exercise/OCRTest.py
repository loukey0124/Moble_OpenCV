import cv2
import pytesseract
from PIL import Image


image = cv2.imread('./data/ocr.jpg', cv2.IMREAD_GRAYSCALE)
_, image = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
cv2.imshow(' ', image)
text = pytesseract.image_to_string(image, 'kor', '--oem 3 --psm 4')
print(text)

cv2.waitKey()
cv2.destroyAllWindows()