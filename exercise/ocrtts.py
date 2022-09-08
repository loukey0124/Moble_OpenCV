from PIL import Image
import pytesseract
 
# pip install speechrecognition
# pip install gTTs  
# pip install playsound==1.2.2
import speech_recognition as sr
from gtts import gTTS
import playsound
 
filename = '.\data\sound.mp3'
def speak(text):
     tts = gTTS(text=text, lang='ko')
     tts.save(filename)
     playsound.playsound(filename)
 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
 
str = pytesseract.image_to_string(Image.open('.\data\sample.jpg'), lang='kor')
 
print(str)
speak(str)