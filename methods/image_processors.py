from docx import Document
import os
from PIL import Image
import io


def resize_and_pad_image(image, target_size=(250, 250), maintain_aspect=True):
    """
    Resizes an image to a target size, optionally maintaining aspect ratio.
    """
    image = image.convert("RGBA")
    white_bg = Image.new("RGBA", image.size, (255, 255, 255, 255))
    image = Image.alpha_composite(white_bg, image).convert("RGB")

    if maintain_aspect:
        original_width, original_height = image.size
        target_width, target_height = target_size

        scale_width = target_width / original_width
        scale_height = target_height / original_height
        scale_factor = min(scale_width, scale_height)

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        final_image = Image.new("RGB", target_size, (255, 255, 255))
        x_offset = round((target_width - new_width) / 2)
        y_offset = round((target_height - new_height) / 2)

        final_image.paste(resized_image, (x_offset, y_offset))
    else:
        final_image = image.resize(target_size, Image.Resampling.LANCZOS)

    return final_image