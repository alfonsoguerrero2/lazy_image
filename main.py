from docx import Document
import os
from PIL import Image
from methods.file_systems import  extract_images_from_docx , save_images
from methods.image_processors import resize_and_pad_image
from methods.file_types import process_docx_images
import io


# Example usage
docx_file = "crisp.docx"
images = process_docx_images(docx_file, output_folder="extracted_images", target_size=(700, 400), maintain_aspect=True)

if images:
    print(f"✅ Found and resized {len(images)} image(s):")
    for img in images:
        print(img)
else:
    print("No images found in the document.")