import numpy as np
import matplotlib.pyplot as plt

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from functions.image_io import read_image
from functions.format_conversion import to8bit
from functions.format_conversion import toFloat
from functions.laplace_filter import apply_laplace_filter
from functions.sobel_gradients import apply_sobel_gradients
from functions.gaussian import apply_gaussian_filter
from functions.intensity_powerlaw import intensityPowerlawLUT


# Read image from tiff file
image_skeleton = read_image('../../data/Fig0343(a)(skeleton_orig).tif')

# # Normalize image values using minmax method to use full [0, 255] range
# image_skeleton = to8bit(toFloat(image_skeleton), mode='minmax')

# Convert image intensity values to float for further processing
image_skeleton_float = toFloat(image_skeleton)

# Acquire Laplacian of the original image
image_skeleton_laplacian = -1. * apply_laplace_filter(image_skeleton_float, type='diagonal')

# Image sharpening using Laplacian and predefined strength constant
image_sharpened_laplacian = image_skeleton_float + image_skeleton_laplacian

# Acquire Sobel gradient of the original image
image_sobel_magnitude = apply_sobel_gradients(image_skeleton_float)

# Smooth Sobel image using Gaussian blur
image_sobel_smooth = apply_gaussian_filter(image_sobel_magnitude, 5)

# Create the mask by multiplying element-wise
image_sharpened_sobel_mask = image_sharpened_laplacian * image_sobel_smooth

# Sharpen the original image using mask with some strength constant
image_sharpened_with_mask = image_skeleton_float + image_sharpened_sobel_mask

# Scale image intensity values to range [0, 255] for power law implementation with LUT
image_sharpened_with_mask_8bit = to8bit(image_sharpened_with_mask, mode='truncate')

# Apply power law to the sharpened image
image_skeleton_final = intensityPowerlawLUT(image_sharpened_with_mask_8bit, gamma=0.4)

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

images = [image_skeleton, to8bit(image_skeleton_laplacian), to8bit(image_sharpened_laplacian),
          to8bit(image_sobel_magnitude), to8bit(image_sobel_smooth), to8bit(image_sharpened_sobel_mask),
          to8bit(image_sharpened_with_mask), image_skeleton_final]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
descriptions = [
    'Original Image',
    'Laplacian of Image (b)',
    'Sharpened Image (a + b)',
    'Sobel Gradient Magnitude',
    'Sobel Image Smoothed',
    'Mask (c x e)',
    'Sharpened with Mask (a + f)',
    'Power Law Transformation'
]

for i, ax in enumerate(axs.ravel()):
    ax.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    ax.axis('off')
    ax.text(0.92, 0.95, labels[i], fontsize=14, color='white', transform=ax.transAxes, ha='center', va='center')
    
plt.tight_layout()
fig.subplots_adjust(wspace=-0.6)
plt.show()

skeleton_powerlaw_only = intensityPowerlawLUT(image_skeleton, gamma=0.4)

images = [image_skeleton, image_skeleton_final, skeleton_powerlaw_only]
titles = ['Original image', 'Multistep processing', 'Power law only']

fig, axs = plt.subplots(1, 3, figsize=(6, 14))

for i in range(3):
    axs[i].imshow(images[i], cmap='gray', vmin=0, vmax=255)
    axs[i].set_title(titles[i], fontsize=10)
    axs[i].axis('off')

plt.tight_layout()
plt.show()