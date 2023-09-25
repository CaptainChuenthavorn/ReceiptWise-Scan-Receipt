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
results = reader.readtext('E-receipt-Dataset\scb\IMG_0766.JPG', paragraph=True, detail=1,add_margin=0.148,
                                          blocklist='๐๑๒๓๔๕๖๗๘๙¥¢¤£*!@#$%^&+|?><', min_size=30)
print(results)

for (bbox, text)in results: 
# unpack the bounding box
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    print(text)
    print(bbox)
    cv2.rectangle(image, tl, br, ( 255,0,0), 3)
plt.rcParams['figure.figsize'] = (16,16)
plt.imshow(image)

img_prefix_name=14
output_filename = f"text_ocr{img_prefix_name}.txt"
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(str(results))
    # for text in results:
    #     file.write(str(text )+ '\n')
    file.write("""(r"temp\krungsri\dilated_image.jpg",paragraph=True,detail=0,decoder='beamsearch',
                          blocklist ='๐๑๒๓๔๕๖๗๘๙¥¢¤£oo*!@#$%^&())_+|?><',min_size =30)\n""")

print("Desired texts have been written to", output_filename)

