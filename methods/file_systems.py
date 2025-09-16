from docx import Document
import os
from PIL import Image
import io


def extract_images_from_docx(docx_path):
    """
    Extracts images from a Word document and returns them as a list of PIL Image objects.
    """
    document = Document(docx_path)
    images = []

    for rel in document.part.related_parts.values():
        if "image" in rel.content_type:
            img_bytes = rel.blob
            image = Image.open(io.BytesIO(img_bytes))
            images.append(image)

    return images


def save_images(images, output_folder="extracted_images"):
    """
    Saves a list of PIL Image objects to the specified output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []

    for i, image in enumerate(images, start=1):
        image_path = os.path.join(output_folder, f"image_{i}.png")
        image.save(image_path, format="PNG")
        image_paths.append(image_path)

    return image_paths
