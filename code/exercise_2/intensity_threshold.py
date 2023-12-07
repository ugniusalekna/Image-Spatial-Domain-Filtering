import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.intensityLUT import intensityLUT

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def intensityThreshold(image, value):
#     # Apply binary thresholding 
#     duplicate_image = np.where(image >= value, 255, 0)
#     return duplicate_image

def intensityThresholdLUT(image, value):
    # Create a duplicate of the original image
    duplicate_image = np.copy(image)
    # Generate a lookup table
    lut = intensityLUT(transform='threshold', threshold=value)
    # Apply the threshold transformation using the lookup table
    duplicate_image = lut[duplicate_image]
    
    return duplicate_image


# Load the original image using libtiff
image_faded_pollen = read_image('../../data/Fig0310(b)(washed_out_pollen_image).tif')

# Apply threshold function to produce a binary image
threshold_faded_pollen_1 = intensityThresholdLUT(image_faded_pollen, 110)

# Create a figure for 1x2 plots
plt.figure(figsize=(8, 4))

# Plot each one of the acquired images
plt.subplot(1, 2, 1)
plt.imshow(threshold_faded_pollen_1, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title('Threshold Value $t=110$')

plt.subplot(1, 2, 2)
plt.imshow(image_faded_pollen, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title('Original Image')

plt.tight_layout()
plt.show()