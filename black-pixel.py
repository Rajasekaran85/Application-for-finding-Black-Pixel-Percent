import numpy as np
from PIL import Image
import os

def calculate_black_pixel_percentage(image_path, threshold=50):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img_gray = img.convert('L')
    
    # Convert to numpy array for efficient pixel manipulation
    img_array = np.array(img_gray)
    
    # Calculate the percentage of black pixels
    black_pixels = np.sum(img_array < threshold)
    total_pixels = img_array.size
    black_percentage = (black_pixels / total_pixels) * 100
    return black_percentage

def find_images_with_black_pixel_concentration(images_folder):
    # Get a list of TIFF images in the specified folder
    tiff_images = [f for f in os.listdir(images_folder) if f.endswith('.tif')]
    
    if not tiff_images:
        print("No TIFF images found in the specified folder.")
        return None
    
    # List to store image paths and their black pixel concentrations
    image_concentrations = []
    
    # Iterate through the TIFF images
    for tiff_image in tiff_images:
        image_path = os.path.join(images_folder, tiff_image)
        
        # Calculate black pixel concentration for the current image
        black_percentage = calculate_black_pixel_percentage(image_path)
        
        # Append the image path and concentration to the list
        image_concentrations.append((image_path, black_percentage))
    
    # Sort the list based on black pixel concentration in descending order
    sorted_images = sorted(image_concentrations, key=lambda x: x[1], reverse=True)
    
    return sorted_images

# Specify the folder containing TIFF images
images_folder = 'D:/German-Federal-Archives/Testing/2024-02-19/ZLA_1_12008482/scanner1'

# Find images and their black pixel concentrations, sorted by concentration
result_images = find_images_with_black_pixel_concentration(images_folder)

if result_images:
    print("Images sorted by black pixel concentration:")
    for image_path, concentration in result_images:
        print(f"{image_path}: {concentration:.2f}%")
else:
    print("No TIFF images found in the specified folder.")
