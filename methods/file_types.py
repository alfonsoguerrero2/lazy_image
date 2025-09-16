from docx import Document
import os
from PIL import Image
import io
from methods.file_systems import  extract_images_from_docx , save_images
from methods.image_processors import resize_and_pad_image

def process_docx_images(docx_path, output_folder="extracted_images", target_size=(250, 250), maintain_aspect=True):
    """
    Processes a Word document to extract, resize, and save images.

    """
    images = extract_images_from_docx(docx_path)

    processed_images = [
        resize_and_pad_image(image, target_size, maintain_aspect)
        for image in images
    ]

    saved_image_paths = save_images(processed_images, output_folder)

    return saved_image_paths