import cv2
import os

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def process_images(directory):
    for folder in os.listdir(directory):
        print("We in Folder",folder)
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            for i, filename in enumerate(os.listdir(folder_path), start=1):
                print("We converting",filename)
                if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.JPG') :
                    image_path = os.path.join(folder_path, filename)
                    img = cv2.imread(image_path)

                    inverted_image = cv2.bitwise_not(img)
                    # cv2.imwrite(f"binarize_temp_manual/inverted_{folder}_{i}.jpg", inverted_image)

                    gray_image = grayscale(img)
                    # cv2.imwrite(f"binarize_temp_manual/gray_{folder}_{i}.jpg", gray_image)


                    thresh, im_bw = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)  
                    #thresh, otsu = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                    cv2.imwrite(f"binarize_temp_manual/bw_image_{folder}_{i}.jpg", im_bw)

# Call the function with the path to your 'E-receipt-Dataset' directory
process_images('E-receipt-Dataset')
