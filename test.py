import os   
import pygetwindow as gw

import tkinter as tk

from PIL import Image
import pytesseract
import numpy as np
from pytesseract import Output
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    if os.path.exists(image_path):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # اعمال فیلتر گوسی برای حذف نویز
        blurred_image = cv2.GaussianBlur(gray_image, (7,7), 0)
        
        # تبدیل تصویر به تصویر سیاه و سفید با استفاده از آستانه‌گذاری دسته‌ای (با استفاده از روش Binary Thresholding)
        _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # اعمال مربع نقشه ریاست برای حذف نویزهای کوچکتر
        kernel = np.ones((3, 3), np.uint8)
        binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
        return binary_image
    else:
        print(f"تصویر '{image_path}' یافت نشد.")
# def preprocess_image2(image_path):
#     if os.path.exists(image_path):
#         image = cv2.imread(image_path)
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#         kernel2 = np.array([[-1, -1, -1], 
#                     [-1, 8, -1], 
#                     [-1, -1, -1]]) 
  
#         # Applying the filter2D() function 
#         blurred_image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2) # اعمال فیلتر گوسی برای حذف نویز
        
#         # تبدیل تصویر به تصویر سیاه و سفید با استفاده از آستانه‌گذاری دسته‌ای (با استفاده از روش Binary Thresholding)
#         _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
#         # اعمال مربع نقشه ریاست برای حذف نویزهای کوچکتر
#         kernel = np.ones((3, 3), np.uint8)
#         binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
#         return binary_image
#     else:
#         print(f"تصویر '{image_path}' یافت نشد.")

# # تابع را فراخوانی و تصویر را پیش‌پردازش کنید
# preprocessed_image = preprocess_image(r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png")
# preprocessed_image2 = preprocess_image2(r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png")
# if preprocessed_image is not None:
#     cv2.imwrite("test.jpg", preprocessed_image)
#     cv2.imwrite("test.jpg", preprocessed_image2)
#     text = str(pytesseract.image_to_string(preprocessed_image)).strip()
#     print(text)
#     cv2.imshow(" ",preprocessed_image)
#     cv2.waitKey(0) 
#     cv2.destroyAllWindows()

# a=cv2.imread(r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png")
# print(np.array(a).shape)

  
# Reading the image 
image = cv2.imread(r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png") 
  
# Creating the kernel(2d convolution matrix) 
kernel2 = np.array([[-1, -1 ,-1], 
                    [8, 8, 8], 
                    [-1, -1, -1]]) 
kernel1 = np.array([[-1, 8 ,-1], 
                    [-1, 8, -1], 
                    [-1, 8, -1]]) 
  
# Applying the filter2D() function 
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2) 
img2 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1) 
img3=  (img//255-img2//255)/2
cv2.imwrite("2d.png",img3)
# print("image 2->",img2)
print("image ->",img3.max())
# a=cv2.imread()
preprocessed_image = preprocess_image(r"C:\Users\h.borgheyi\Desktop\Web Scraper\2d.png")
text = str(pytesseract.image_to_string(preprocessed_image)).strip()
print(text)
# Shoeing the original and output image 
cv2.imshow('Original', image) 
# cv2.imshow('Kernel Blur1', img) 
# cv2.imshow('Kernel Blur2', img2) 
cv2.imshow('Kernel Blur', img3*255) 
cv2.imshow('preprocessed_image ', preprocessed_image) 
  
cv2.waitKey() 
cv2.destroyAllWindows() 