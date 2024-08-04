from PIL import Image
import os

def optimize_image(image_path, output_path, quality=85):
    print(f"Current working directory: {os.getcwd()}")
    print(f"Image path: {image_path}")
    if os.path.exists(image_path):
        print(f"File {image_path} exists.")
    else:
        print(f"File {image_path} does not exist.")
    with Image.open(image_path) as img:
        img.save(output_path, 'JPEG', optimize=True, quality=quality)

# Example usage with the correct file name
optimize_image('C:/Users/inc/Documents/GitHub/Honor-qr/public/images/input.jpg', 'C:/Users/inc/Documents/GitHub/Honor-qr/public/images/output.jpg')
