from docx import Document
import os
from PIL import Image
import io

def extract_and_resize_images(docx_path, output_folder="extracted_images", target_size=(250, 250), maintain_aspect=True):
    """
    Extracts images from a Word document, resizes them while maintaining aspect ratio, and saves to a folder.

    :param docx_path: Path to the Word (.docx) file.
    :param output_folder: Folder to save resized images.
    :param target_size: Tuple (width, height) for the maximum size in pixels.
    :param maintain_aspect: If True, maintains aspect ratio with padding. If False, stretches to exact size.
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

            if maintain_aspect:
                # Calculate the aspect ratio preserving size
                original_width, original_height = image.size
                target_width, target_height = target_size
                
                # Calculate scaling factor (use the smaller ratio to fit within bounds)
                scale_width = target_width / original_width
                scale_height = target_height / original_height
                scale_factor = min(scale_width, scale_height)
                
                # Calculate new size maintaining aspect ratio
                new_width = int(original_width * scale_factor)
                new_height = int(original_height * scale_factor)
                
                # Resize image maintaining aspect ratio
                resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Create a new image with target size and white background
                final_image = Image.new("RGB", target_size, (255, 255, 255))
                
                # Calculate position to center the resized image (using precise centering)
                x_offset = (target_width - new_width) / 2
                y_offset = (target_height - new_height) / 2
                
                # Round to nearest pixel for precise centering
                x_offset = round(x_offset)
                y_offset = round(y_offset)
                
                # Paste the resized image onto the white background
                final_image.paste(resized_image, (x_offset, y_offset))
            else:
                # Stretch to exact target size (original behavior)
                final_image = image.resize(target_size, Image.Resampling.LANCZOS)

            # Save image
            image_path = os.path.join(output_folder, f"image_{i}.png")
            final_image.save(image_path, format="PNG")
            images_found.append(image_path)
            
            if maintain_aspect:
                print(f"Image {i}: Original {image.size} -> Fitted to {target_size} (actual content: {new_width}x{new_height})")
            else:
                print(f"Image {i}: Original {image.size} -> Stretched to {target_size}")

    return images_found


# Example usage with aspect ratio preservation (default):
#Find sweet spot for size, recommended to find size of orginal images within document first and use those dimensions, will convert all pictures to size
#Insert borders where necessary to maintain aspect ratio
docx_file = "target2.docx"
images = extract_and_resize_images(docx_file, output_folder="extracted_images2", target_size=(700, 400), maintain_aspect=True)

# Alternative: if you want the old stretching behavior:
# images = extract_and_resize_images(docx_file, output_folder="extracted_images", target_size=(400, 400), maintain_aspect=False)

if images:
    print(f"✅ Found and resized {len(images)} image(s):")
    for img in images:
        print(img)
else:
    print("No images found in the document.")