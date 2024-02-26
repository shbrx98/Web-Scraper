import os   
import tkinter as tk
from PIL import Image
import pytesseract
import numpy as np
import cv2
from pytesseract import Output
import matplotlib.pyplot as plt

# مسیرهای مربوط به فایل‌ها
IMAGE_PATH = r"C:\Users\h.borgheyi\Desktop\Web Scraper\Screenshot\screenshot.png"
PREPROCESSED_IMAGE_PATH = r"C:\Users\h.borgheyi\Desktop\Web Scraper\preprocessed_image.png"


def preprocess_image(image_path):
    if os.path.exists(image_path):
        # خواندن تصویر
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

def read_text_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    text = str(pytesseract.image_to_string(preprocessed_image)).strip()
    return text


def main():
    # Reading the image 
    image = cv2.imread(IMAGE_PATH) 
    
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
    img3 = (img // 255 - img2 // 255) / 2
    
    # ذخیره تصویر پس از پیش‌پردازش
    cv2.imwrite("2d.png", img3)
    print("image ->", img3.max())
    
    # خواندن متن از تصویر
    text = read_text_from_image(r"C:\Users\h.borgheyi\Desktop\Web Scraper\2d.png")
    print(text)
    
    # نمایش تصاویر با استفاده از Matplotlib
    plt.figure(figsize=(10, 5))
    
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title("Original")
    plt.axis("off")
    
    plt.subplot(2, 2, 2)
    plt.imshow(img)
    plt.title("Kernel Blur1")
    plt.axis("off")
    
    plt.subplot(2, 2, 3)
    plt.imshow(img2)
    plt.title("Kernel Blur2")
    plt.axis("off")
    
    plt.subplot(2, 2, 4)
    plt.imshow(img3 * 255)
    plt.title("Kernel Blur")
    plt.axis("off")
    
    plt.show()

if __name__ == "__main__":
    main()
