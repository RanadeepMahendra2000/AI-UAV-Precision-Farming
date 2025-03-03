import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------ STEP 1: Data Ingestion & Cleaning ------------------

def organize_images(input_folder, output_folder):
    """Sort images into structured folders based on metadata."""
    for file in os.listdir(input_folder):
        if file.endswith((".jpg", ".png", ".tif")):
            filepath = os.path.join(input_folder, file)
            try:
                date_taken = "2024-03-01"  # Simulated metadata
                folder_name = date_taken.replace(":", "-").split(" ")[0]
                output_path = os.path.join(output_folder, folder_name)
                
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                os.rename(filepath, os.path.join(output_path, file))
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Run organization
organize_images("raw_uav_images", "structured_data")

# ------------------ STEP 2: Image Preprocessing ------------------

def preprocess_image(image_path):
    """Apply noise reduction, grayscale conversion, and resizing."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (512, 512))
    return resized_image

# Example usage
preprocessed_img = preprocess_image("structured_data/2024-03-01/image_001.jpg")
cv2.imwrite("processed_data/preprocessed_image.jpg", preprocessed_img)

# ------------------ STEP 3: NDVI Computation ------------------

def compute_ndvi(nir_path, red_path):
    """Compute NDVI using NIR and Red channels."""
    nir = cv2.imread(nir_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    red = cv2.imread(red_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    
    ndvi = (nir - red) / (nir + red + 1e-10)
    
    # Normalize NDVI values
    ndvi_normalized = cv2.normalize(ndvi, None, 0, 255, cv2.NORM_MINMAX)
    ndvi_colormap = cv2.applyColorMap(ndvi_normalized.astype(np.uint8), cv2.COLORMAP_JET)
    
    return ndvi_colormap, ndvi

# Compute NDVI
ndvi_result, ndvi_values = compute_ndvi("processed_data/nir_image.png", "processed_data/red_image.png")
cv2.imwrite("processed_data/ndvi_result.jpg", ndvi_result)

print("✅ NDVI Computation Completed Successfully!")
