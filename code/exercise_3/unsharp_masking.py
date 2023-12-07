import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.format_conversion import to8bit
from functions.format_conversion import toFloat
from functions.gaussian import apply_gaussian_filter

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Read an image for the exercise
image_dipxe = read_image('../../data/Fig0340(a)(dipxe_text).tif')

# Normalize image values using minmax method to use full [0, 255] range
image_dipxe = to8bit(toFloat(image_dipxe), mode='minmax')

# Apply the multistep unsharp masking
image_dipxe_float = toFloat(image_dipxe)

# Blur the original image
image_dipxe_blur = apply_gaussian_filter(image_dipxe_float, filter_size=15)

# Subtract blurred image from original
blur_difference_mask = image_dipxe_float - image_dipxe_blur

# Add mask to original
strength = 10
image_dipxe_sharpened = image_dipxe_float + strength * blur_difference_mask

image_dipxe_sharpened_8bit = to8bit(image_dipxe_sharpened, mode='truncate')

plt.figure(figsize=(8, 4))

plt.subplot(2, 2, 1)
plt.imshow(image_dipxe, cmap='gray', vmin=0, vmax=255)
plt.title('Original image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(to8bit(image_dipxe_blur, mode='minmax'), cmap='gray', vmin=0, vmax=255)
plt.title('Blurred image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(to8bit(blur_difference_mask, mode='minmax'), cmap='gray', vmin=0, vmax=255)
plt.title('Mask')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(image_dipxe_sharpened_8bit, cmap='gray', vmin=0, vmax=255)
plt.title('Sharpened image')
plt.axis('off')

plt.tight_layout()
plt.show()