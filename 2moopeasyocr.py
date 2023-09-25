import os
import easyocr
import torch

# Load the Thai model from the thai.pth file
model_path = 'thai.pth'  # Replace 'path_to_thai.pth' with the actual path to your thai.pth file
model = torch.load(model_path, map_location='cpu')

# Create an EasyOCR reader instance with the loaded model
reader = easyocr.Reader(lang_list=['th', 'en'], model_storage_directory='.')

# Define the root directory where your subfolders are located
root_directory = 'E-receipt-Dataset'

# Iterate through subfolders
for subfolder in os.listdir(root_directory):
    subfolder_path = os.path.join(root_directory, subfolder)

    # Check if it's a directory
    if os.path.isdir(subfolder_path):
        # Iterate through image files in the subfolder
        for image_name in os.listdir(subfolder_path):
            if image_name.endswith('.JPG'):
                image_path = os.path.join(subfolder_path, image_name)
                print(image_path)                
                # Read text from the image
                results = reader.readtext(image_path, paragraph=True, detail=1,add_margin=0.148,
                                          blocklist='๐๑๒๓๔๕๖๗๘๙¥¢¤£*!@$^+|?><', min_size=30)
                
                # Define the output text file name
                output_filename = f"Pre_text_ocr_{subfolder}_{image_name}.txt"
                
                # Write the OCR results to the text file
                with open(output_filename, 'w', encoding='utf-8') as file:
                    for text in results:
                        file.write(str(text) + '\n')
                    # file.write(f"""\n({image_path}image_path, paragraph=True, detail=1,
                    #                       blocklist='๐๑๒๓๔๕๖๗๘๙¥¢¤£oo*!@#$%^&())_+|?><', min_size=30\n""")
                
                print(f"Text from {image_name} in {subfolder} has been written to {output_filename}")
