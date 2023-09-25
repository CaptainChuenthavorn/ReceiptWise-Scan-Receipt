import easyocr
import torch
import cv2
import matplotlib.pyplot as plt
# Load the Thai model from the thai.pth file
model_path = 'thai.pth'  # Replace 'path_to_thai.pth' with the actual path to your thai.pth file
model = torch.load(model_path, map_location='cpu')

# Create an EasyOCR reader instance with the loaded model
reader = easyocr.Reader(lang_list=['th','en'], model_storage_directory='.')
image = cv2.imread(r"E-receipt-Dataset\scb\IMG_0793.JPG")
# Replace 'your_image.jpg' with the path to your image containing Thai text
results = reader.readtext(image,paragraph=True,detail=1,add_margin=0.148,
                          blocklist ='๐๑๒๓๔๕๖๗๘๙¥¢¤£oo*!@#$%^&())_+|?><',min_size =30)
print(results)
