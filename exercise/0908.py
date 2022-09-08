import cv2 as cv
import pafy

url = "https://www.youtube.com/watch?v=433HGrqXk_k&t=110s&ab_channel=M2"
video = pafy.new(url)
best = video.getbest(preftype = 'any')

webCAM = cv.VideoCapture(best.url)
 
# 'q' 키 입력될 때까지 계속 실행
while True:
 
    # step1) webCAM 이미지 준비
    ret, image = webCAM.read()
    
    vid_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    vid_blur = cv.medianBlur(vid_gray, 5)
    vid_edge = cv.adaptiveThreshold(vid_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize=9, C=3)
    
    cv.imshow('webCAM', vid_edge)
 
    # 키 입력 확인
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
       
webCAM.release()
cv.destroyAllWindows()