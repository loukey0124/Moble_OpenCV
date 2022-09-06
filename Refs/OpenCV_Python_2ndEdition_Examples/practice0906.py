import cv2
import numpy as np
import matplotlib as plt

alpha = 0.3
imageFile = "./data/Lena.bmp"
img = cv2.imread(imageFile)

cap = cv2.VideoCapture("./data/vtest.avi")
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#img = cv2.resize(img, (768, 576))
# while True:   
#     retval, frame = cap.read()
#     if not retval:
#         break
    
#     addimg = frame * (1 - alpha) + img * alpha
#     addimg = addimg.astype(np.uint8)
#     cv2.imshow('frame', addimg)
    
#     key = cv2.waitKey(25)
#     if key == 27: # Esc
#         break
# if cap.isOpened():
#     cap.release()
    
# cv2.destroyAllWindows()

#==================================
# img = cv2.resize(img, (100, 100))
# h, w, c = img.shape
# mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# mask[mask[:]==255]=0
# mask[mask[:]>0]=255
# mask_inv = cv2.bitwise_not(mask)
# lena = cv2.bitwise_and(img, img, mask=mask)

# while True:   
#     retval, frame = cap.read()
#     if not retval:
#         break
    
#     roi = frame[100:100+h, 100:100+w]
#     back = cv2.bitwise_and(roi, roi, mask=mask_inv)
#     dst = cv2.add(lena, back)
#     frame[100:100+h, 100:100+w] = dst    
#     cv2.imshow('frame', frame)
    
#     key = cv2.waitKey(25)
#     if key == 27: # Esc
#         break
# if cap.isOpened():
#     cap.release()
    
# cv2.destroyAllWindows()

#==================================
img = cv2.resize(img, (100, 100))
h, w, c = img.shape

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    
    roi = frame[100:100+h, 100:100+w]
    
    dst = roi*(1-alpha)+img*alpha
    frame[100:100+h, 100:100+w] = dst    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()