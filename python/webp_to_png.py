import os
from PIL import Image

def convert_webp_to_png(source_webp, output_png):
    """
    Convert a WEBP image file to a PNG file.

    Args:
    source_webp (str): The path to the WEBP image file.
    output_png (str): The path where the PNG image file will be saved.
    """
    # Open the WEBP image file
    with Image.open(source_webp) as image:
        # Convert the image to 'RGB' mode if it is not
        if image.mode != 'RGB':
            image = image.convert('RGB')
        # Save the image as a PNG file
        image.save(output_png, 'PNG')
        
# for all webp images in images/webp create one png image in images/png
if __name__ == '__main__':
    for file in os.listdir('images/webp'):
        if file.endswith('.webp'):
            convert_webp_to_png(f'images/webp/{file}', f'images/png/{file[:-5]}.png')
