import pytesseract
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

class ExtractTextFromImage:
    @staticmethod
    def execute(file):
        image = Image.open(file)
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)  
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] 

        text = pytesseract.image_to_string(threshold_img)
        return text