# import pytesseract
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import easyocr
import cv2
import matplotlib.pyplot as plt
from PIL import Image,ImageFont,ImageDraw
import numpy as np
img=cv2.imread(r"temp\dilated_image.jpg")
# cv2.imshow("window",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# text = pytesseract.image_to_string(img, lang='tha+eng')

font_path = 'fonts\THSarabunNew.ttf'  # Replace with the actual path to the Thai font
font = ImageFont.truetype(font_path,50)

# font.loadFontData(font_path)
b,g,r,a = 0,255,0,0


reader = easyocr.Reader(['th','en'],gpu=False)
result = reader.readtext(img,paragraph=True,detail=0 )
print(result)
img_prefix_name=1
# Write the desired texts to a file
output_filename = f"text_ocr{img_prefix_name}.txt"
with open(output_filename, 'w', encoding='utf-8') as file:
    for text in result:
        file.write(text + '\n')

print("Desired texts have been written to", output_filename)
# for t in result:
#     print(t)

#     bbox,text,score = t

#     # cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
#     # cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
#     img_pil = Image.fromarray(img)
#     draw = ImageDraw.Draw(img_pil)
#     draw.text(bbox[0],text, font = font, fill = (255, 0, 255, a))
#     img = np.array(img_pil)

# plt.imshow(img)
# plt.show()
# plt.savefig('foo.png')