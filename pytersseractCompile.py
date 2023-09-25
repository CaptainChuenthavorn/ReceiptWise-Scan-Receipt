
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import cv2
img=cv2.imread(r"temp\Screenshot 2023-07-31 111434.png")
# cv2.imshow("window",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
text = pytesseract.image_to_string(img, lang='tha+eng')
print(text)