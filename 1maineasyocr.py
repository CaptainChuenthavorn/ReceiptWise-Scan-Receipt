import cv2
import numpy
from matplotlib import pyplot as plt
import easyocr
from PIL import Image,ImageFont,ImageDraw
import numpy as np

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)

def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2),np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)

image_file = r"S__49684702.jpg"
img = cv2.imread(image_file)
# gray scale
gray_image = grayscale(img)
thresh, otsu = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
no_noise = noise_removal(otsu)
dilated_image = thick_font(no_noise)
cv2.imwrite("temp/dilated_image.jpg", dilated_image)


img=cv2.imread(dilated_image)

# Initialize EasyOCR reader
reader = easyocr.Reader(['th', 'en'], gpu=False)

# Create a list to store the desired texts and image paths
desired_texts = []
image_paths = []

# Write the desired texts to a file
output_filename = f"text_ocr{img_prefix_name}.txt"
with open(output_filename, 'w', encoding='utf-8') as file:
    for text in desired_texts:
        file.write(text + '\n')

print("Desired texts have been written to", output_filename)