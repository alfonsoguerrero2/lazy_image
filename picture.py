from docx import Document
import os
from PIL import Image
import io

def extract_and_resize_images(docx_path, output_folder="extracted_images", target_size=(250, 250)):
    """
    Extracts images from a Word document, resizes them to the same size, and saves to a folder.

    :param docx_path: Path to the Word (.docx) file.
    :param output_folder: Folder to save resized images.
    :param target_size: Tuple (width, height) for resizing in pixels.
    :return: List of saved image file paths.
    """
    document = Document(docx_path)
    images_found = []

    os.makedirs(output_folder, exist_ok=True)

    for i, rel in enumerate(document.part.related_parts.values(), start=1):
        if "image" in rel.content_type:
            img_bytes = rel.blob
            image = Image.open(io.BytesIO(img_bytes))

            # Convert to RGBA to handle transparency
            image = image.convert("RGBA")

            # Create white background and alpha-composite for smooth edges
            white_bg = Image.new("RGBA", image.size, (255, 255, 255, 255))
            image = Image.alpha_composite(white_bg, image)

            # Convert back to RGB (no alpha channel left)
            image = image.convert("RGB")

            # Resize to target size
            resized_image = image.resize(target_size)

            # Save image
            image_path = os.path.join(output_folder, f"image_{i}.png")
            resized_image.save(image_path, format="PNG")
            images_found.append(image_path)

    return images_found


# Example usage:
docx_file = "crisp.docx"
images = extract_and_resize_images(docx_file, output_folder="extracted_images", target_size=(400, 400))

if images:
    print(f"✅ Found and resized {len(images)} image(s):")
    for img in images:
        print(img)
else:
    print("No images found in the document.")
