import cv2
import numpy
from matplotlib import pyplot as plt


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_file = "E-receipt-Dataset\K-bank\S__6275225.jpg"
img = cv2.imread(image_file)

inverted_image = cv2.bitwise_not(img)
cv2.imwrite("temp/inverted.jpg", inverted_image)


gray_image = grayscale(img)
cv2.imwrite("temp/gray.jpg", gray_image)

#thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
thresh, otsu = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("temp/bw_image.jpg", otsu)