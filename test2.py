#!/usr/bin/env python
# coding: utf-8

# In[14]:


#pip install PyPDF2==2.12.1


# In[10]:


#pip install easyocr


# In[3]:


#pip install PIP


# In[2]:


# import PyPDF2
# import os
# from PIL import Image
# import io

# final={}

# def extract_images_from_pdf(pdf_path, output_path):
#     pdf_document = PyPDF2.PdfFileReader(pdf_path)
#     for current_page_number in range(pdf_document.getNumPages()):
#         current_page = pdf_document.getPage(current_page_number)
#         if "/XObject" in current_page["/Resources"]:
#             x_object = current_page["/Resources"]["/XObject"].getObject()
#             for obj in x_object:
#                 if x_object[obj]["/Subtype"] == "/Image":
#                     image = x_object[obj]
#                     image_bytes = image._data
#                     image = Image.open(io.BytesIO(image_bytes))
#                     image.save(os.path.join(output_path, f"{current_page_number}.png"))

# def ocr_on_images(images_folder_path):
#     reader = easyocr.Reader(["en"])
#     for image_name in os.listdir(images_folder_path):
#         image_path = os.path.join(images_folder_path, image_name)
#         image = Image.open(image_path)

#         #crop the image to get the required coordinates x1=668, y1=1112, x2=2740, y2=1390
#         image = image.crop((668, 1112, 2740, 1390))
#         image = np.array(image)
#         result = reader.readtext(image)
        
#         # for detection in result:
#         #     if detection[0][1] >= 668 and detection[0][3] <= 1112:
#         #         print(f"Text between coordinates 668, 1112, 2740, 1390 is: {detection[1]}")
#         if result==[]:
#             print(image_name[0], "No text found")
            
#         else:
#             print(image_name[0], result[0][1])

#         final[image_name[0]]="No text found" if result==[] else result[0][1]


#     print(final)
#         # sort the dictionary according to keys
#     key_list=sorted(final.keys())
#     sorted_dict = {}
#     for key in key_list:
#         sorted_dict[key] = final[key]

#     print(sorted_dict)

#     flg=0


#     for key in sorted_dict:
#         if sorted_dict[key]=="COMPLAINT":
#             #store {key}.png in complaint folder
#             image = Image.open(f"./output/{key}.png")
#             image.save(f"./complaint/{key}.png")
#             flg=1

#         elif sorted_dict[key]=="SUMMONS":
#             #store {key}.png in summons folder
#             image = Image.open(f"./output/{key}.png")
#             image.save(f"./summons/{key}.png")
#             flg=2

#         elif sorted_dict[key]=="Appearance By Attorney In Civil Case":
#             #store {key}.png in attorney folder
#             image = Image.open(f"./output/{key}.png")
#             image.save(f"./appearance/{key}.png")
#             flg=3

#         else:
#             if flg==1:
#                 image = Image.open(f"./output/{key}.png")
#                 image.save(f"./complaint/{key}.png")

#             elif flg==2:
#                 image = Image.open(f"./output/{key}.png")
#                 image.save(f"./summons/{key}.png")

#             elif flg==3:
#                 image = Image.open(f"./output/{key}.png")
#                 image.save(f"./appearance/{key}.png")

# def images_to_pdf(folder_path, output_pdf):
#     image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
#     images = [Image.open(image) for image in image_paths]
#     images[0].save(output_pdf, save_all=True, append_images=images[1:])

# if __name__ == "__main__":
#     pdf_path = "123456.pdf"
#     output_path = "./output"
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)
#     extract_images_from_pdf(pdf_path, output_path)
#     print(f"Images extracted from {pdf_path} and saved in {output_path} folder")
    
#     images_folder_path = "./output"
#     ocr_on_images(images_folder_path)

#     # Naming output PDF files
#     input_pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Extracting input PDF file name without extension
#     folders = ["complaint", "summons", "appearance"]
#     for folder in folders:
#         output_pdf = f"{input_pdf_name}_{folder}.pdf"
#         images_to_pdf(folder, output_pdf)


# In[3]:


# import PyPDF2
# import os
# from PIL import Image
# import io
# import easyocr
# import numpy as np
# import configparser

# def extract_images_from_pdf(pdf_path, output_path):
#     pdf_document = PyPDF2.PdfFileReader(pdf_path)
#     for current_page_number in range(pdf_document.getNumPages()):
#         current_page = pdf_document.getPage(current_page_number)
#         if "/XObject" in current_page["/Resources"]:
#             x_object = current_page["/Resources"]["/XObject"].getObject()
#             for obj in x_object:
#                 if x_object[obj]["/Subtype"] == "/Image":
#                     image = x_object[obj]
#                     image_bytes = image._data
#                     image = Image.open(io.BytesIO(image_bytes))
#                     image.save(os.path.join(output_path, f"{current_page_number}.png"))

# # def images_to_pdf(folder_path, output_pdf):
# #     image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
# #     images = [Image.open(image) for image in image_paths]
# #     images[0].save(output_pdf, save_all=True, append_images=images[1:])

# def images_to_pdf(folder_path, output_pdf):
#     # List all image files in the folder and sort them by their file names
#     image_paths = sorted(
#         [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))],
#         key=lambda x: int(os.path.splitext(os.path.basename(x))[0])  # Sort by converting the file names (sans extension) to integers
#     )
#     # Open images
#     images = [Image.open(image) for image in image_paths]
#     # Save all images into one PDF file
#     if images:
#         images[0].save(output_pdf, save_all=True, append_images=images[1:])

# def ocr_on_images(images_folder_path, config):
#     reader = easyocr.Reader(["en"])
    
#     complaint_output = config['Files']['COMPLAINT_OUTPUT']
#     summons_output = config['Files']['SUMMONS_OUTPUT']
#     appearance_output = config['Files']['APPEARANCE_OUTPUT']
    
#     ocr_location = config['OCR']['Loc1'].split(',')
#     x1, y1, x2, y2 = map(int, ocr_location)
    
#     for image_name in os.listdir(images_folder_path):
#         image_path = os.path.join(images_folder_path, image_name)
#         image = Image.open(image_path)

#         # Crop the image based on the OCR location provided in the configuration file
#         image = image.crop((x1, y1, x2, y2))
#         image = np.array(image)
#         result = reader.readtext(image)

#         if result == []:
#             print(image_name[0], "No text found")
#         else:
#             print(image_name[0], result[0][1])

#         final[image_name[0]] = "No text found" if result == [] else result[0][1]

#     # Sort the dictionary according to keys
#     key_list = sorted(final.keys())
#     sorted_dict = {}
#     for key in key_list:
#         sorted_dict[key] = final[key]

#     flg = 0

#     for key in sorted_dict:
#         if sorted_dict[key] == "COMPLAINT":
#             # Store {key}.png in complaint folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(complaint_output, f"{key}.png"))
#             flg = 1

#         elif sorted_dict[key] == "SUMMONS":
#             # Store {key}.png in summons folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(summons_output, f"{key}.png"))
#             flg = 2

#         elif sorted_dict[key] == "Appearance By Attorney In Civil Case":
#             # Store {key}.png in appearance folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(appearance_output, f"{key}.png"))
#             flg = 3

#         else:
#             if flg == 1:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(complaint_output, f"{key}.png"))

#             elif flg == 2:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(summons_output, f"{key}.png"))

#             elif flg == 3:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(appearance_output, f"{key}.png"))


# if __name__ == "__main__":
#     # Load the configuration file
#     config = configparser.ConfigParser()
#     config.read('config.cfg')  # Replace 'config.cfg' with the path to your configuration file
    
#     # Extract input and output paths from the configuration file
#     pdf_path = config['Files']['INPUT']
#     output_path = config['Files']['OUTPUT']
    
#     # Create the output directory if it doesn't exist
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)
    
#     # Extract images from PDF
#     extract_images_from_pdf(pdf_path, output_path)
#     print(f"Images extracted from {pdf_path} and saved in {output_path} folder")
    
#     # Perform OCR on images
#     images_folder_path = output_path
#     ocr_on_images(images_folder_path, config)

#     # Convert separated images to PDFs for each category
#     for folder, output_folder in [("complaint", config['Files']['COMPLAINT_OUTPUT']), 
#                                   ("summons", config['Files']['SUMMONS_OUTPUT']), 
#                                   ("appearance", config['Files']['APPEARANCE_OUTPUT'])]:
#         output_pdf = os.path.join(output_path, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_{folder}.pdf")
#         images_to_pdf(output_folder, output_pdf)


# In[11]:


# import PyPDF2
# import os
# from PIL import Image
# import io
# import easyocr
# import numpy as np
# import configparser

# final={}

# def extract_images_from_pdf(pdf_path, output_path):
#     pdf_document = PyPDF2.PdfFileReader(pdf_path)
#     for current_page_number in range(pdf_document.getNumPages()):
#         current_page = pdf_document.getPage(current_page_number)
#         if "/XObject" in current_page["/Resources"]:
#             x_object = current_page["/Resources"]["/XObject"].getObject()
#             for obj in x_object:
#                 if x_object[obj]["/Subtype"] == "/Image":
#                     image = x_object[obj]
#                     image_bytes = image._data
#                     image = Image.open(io.BytesIO(image_bytes))
#                     image.save(os.path.join(output_path, f"{current_page_number}.png"))

# # def images_to_pdf(folder_path, output_pdf):
# #     image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
# #     images = [Image.open(image) for image in image_paths]
# #     images[0].save(output_pdf, save_all=True, append_images=images[1:])

# def images_to_pdf(folder_path, output_pdf):
#     # List all image files in the folder and sort them by their file names
#     image_paths = sorted(
#         [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))],
#         key=lambda x: int(os.path.splitext(os.path.basename(x))[0])  # Sort by converting the file names (sans extension) to integers
#     )
#     # Open images
#     images = [Image.open(image) for image in image_paths]
#     # Save all images into one PDF file
#     if images:
#         images[0].save(output_pdf, save_all=True, append_images=images[1:])

# def ocr_on_images(images_folder_path, config):
#     reader = easyocr.Reader(["en"])
    
#     complaint_output = config['Files']['COMPLAINT_OUTPUT']
#     summons_output = config['Files']['SUMMONS_OUTPUT']
#     appearance_output = config['Files']['APPEARANCE_OUTPUT']
    
#     ocr_location = config['OCR']['Loc1'].split(',')
#     x1, y1, x2, y2 = map(int, ocr_location)
    
#     for image_name in os.listdir(images_folder_path):
#         image_path = os.path.join(images_folder_path, image_name)
#         image = Image.open(image_path)

#         # Crop the image based on the OCR location provided in the configuration file
#         image = image.crop((x1, y1, x2, y2))
#         image = np.array(image)
#         result = reader.readtext(image)

#         if result == []:
#             print(image_name[0], "No text found")
#         else:
#             print(image_name[0], result[0][1])

#         final[image_name[0]] = "No text found" if result == [] else result[0][1]

#     # Sort the dictionary according to keys
#     key_list = sorted(final.keys())
#     sorted_dict = {}
#     for key in key_list:
#         sorted_dict[key] = final[key]

#     flg = 0

#     for key in sorted_dict:
#         if sorted_dict[key] == "COMPLAINT":
#             # Store {key}.png in complaint folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(complaint_output, f"{key}.png"))
#             flg = 1

#         elif sorted_dict[key] == "SUMMONS":
#             # Store {key}.png in summons folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(summons_output, f"{key}.png"))
#             flg = 2

#         elif sorted_dict[key] == "Appearance By Attorney In Civil Case":
#             # Store {key}.png in appearance folder
#             image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#             image.save(os.path.join(appearance_output, f"{key}.png"))
#             flg = 3

#         else:
#             if flg == 1:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(complaint_output, f"{key}.png"))

#             elif flg == 2:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(summons_output, f"{key}.png"))

#             elif flg == 3:
#                 image = Image.open(os.path.join(images_folder_path, f"{key}.png"))
#                 image.save(os.path.join(appearance_output, f"{key}.png"))


# if __name__ == "__main__":
#     # Load the configuration file
#     config = configparser.ConfigParser()
#     config.read('config.cfg')  # Replace 'config.cfg' with the path to your configuration file
    
#     # Extract input and output paths from the configuration file
#     pdf_path = config['Files']['INPUT']
#     print(pdf_path)
#     images_folder_path = config['Files']['IMAGES']
#     output_path = config['Files']['OUTPUT']
    
#     # Create the output directory if it doesn't exist
#     # if not os.path.exists(output_path):
#     #     os.makedirs(output_path)
    
#     # Extract images from PDF
#     extract_images_from_pdf(pdf_path, images_folder_path)
#     print(f"Images extracted from {pdf_path} and saved in {output_path} folder")
    
#     # Perform OCR on images
#     ocr_on_images(images_folder_path, config)

#     # Convert separated images to PDFs for each category
#     for folder, output_folder in [("complaint", config['Files']['COMPLAINT_OUTPUT']), 
#                                   ("summons", config['Files']['SUMMONS_OUTPUT']), 
#                                   ("appearance", config['Files']['APPEARANCE_OUTPUT'])]:
#         output_pdf = os.path.join(output_path, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_{folder}.pdf")
#         images_to_pdf(output_folder, output_pdf)


# In[17]:


import PyPDF2
import io
from PIL import Image
import easyocr
import numpy as np
import configparser
import os

def extract_images_from_pdf(pdf_path):
    images = []
    pdf_document = PyPDF2.PdfFileReader(pdf_path)
    for current_page_number in range(pdf_document.getNumPages()):
        current_page = pdf_document.getPage(current_page_number)
        if "/XObject" in current_page["/Resources"]:
            x_object = current_page["/Resources"]["/XObject"].getObject()
            for obj in x_object:
                if x_object[obj]["/Subtype"] == "/Image":
                    image = x_object[obj]
                    image_bytes = image._data
                    images.append(Image.open(io.BytesIO(image_bytes)))
    return images

def images_to_pdf(images, output_pdf):
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])

def categorize_images(images, config):
    reader = easyocr.Reader(["en"])
    ocr_location = config['OCR']['Loc1'].split(',')
    x1, y1, x2, y2 = map(int, ocr_location)

    categorized_images = {
        "Complaint": [],
        "Summons": [],
        "Appearance": []
    }
    current_category = None

    for image in images:
        cropped_image = image.crop((x1, y1, x2, y2))
        results = reader.readtext(np.array(cropped_image))
        for result in results:
            text = result[1].upper()
            print(f"Detected OCR Text: {text}")  # Debugging aid
            if "COMPLAINT" in text:
                current_category = "Complaint"
                break
            elif "SUMMONS" in text:
                current_category = "Summons"
                break
            elif "APPEARANCE" in text:
                current_category = "Appearance"
                break

        if current_category:
            categorized_images[current_category].append(image)

    return categorized_images

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.cfg')  # Assume the configuration file path is correct

    pdf_path = config['Files']['INPUT']
    output_path = config['Files']['OUTPUT']

    images = extract_images_from_pdf(pdf_path)
    print(f"Extracted {len(images)} images from {pdf_path}")

    categorized_images = categorize_images(images, config)

    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]

    for category, imgs in categorized_images.items():
        output_pdf_path = f"{output_path}/{base_filename}_{category}.pdf"
        images_to_pdf(imgs, output_pdf_path)
        print(f"Generated PDF for {category} at {output_pdf_path}")


# In[ ]:




