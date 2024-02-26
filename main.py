import os   
import pygetwindow as gw
import pyautogui
import tkinter as tk
import time
from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import cv2
import numpy as np




  





firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
# firefox_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk"

firefox_delay = 5

load_delay = 5

dir_img = r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png"
url = "https://row7.vfsglobal.com/Global-Appointment/"
print(url)
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

os.startfile(firefox_path)


time.sleep(firefox_delay)





pyautogui.click(811, 32)

pyautogui.typewrite(url)
pyautogui.press('enter')

# pyautogui.press('enter')

time.sleep(load_delay)


screenshot = pyautogui.screenshot()


left = 730
top = 545
right = 925
bottom = 620


cropped_image = screenshot.crop((left, top, right, bottom))


cropped_image.save(dir_img)


cropped_image.show()



def preprocess_image(image):
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    return binary_image

preprocessed_image = preprocess_image(cropped_image)
cv2.imwrite("test.jpg", preprocessed_image)


text = str(pytesseract.image_to_string(preprocessed_image)).strip()

pyautogui.click(1020, 585)
print(text)
pyautogui.typewrite(text)
# pyautogui.press('enter')
# pyautogui.click(251, 645)



# results = pytesseract.image_to_data(preprocessed_image, output_type=Output.DICT)
# for i in range(0, len(results['text'])):
#     x = results['left'][i]
#     y = results['top'][i]
#     w = results['width'][i]
#     h = results['height'][i]
#     text = results['text'][i]
#     conf = int(results['conf'][i])    
#     if conf > 58:
#         text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
#         cv2.rectangle(preprocessed_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(preprocessed_image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
# cv2.imshow(" ", preprocessed_image)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()