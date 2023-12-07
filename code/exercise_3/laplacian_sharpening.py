import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.format_conversion import to8bit
from functions.format_conversion import toFloat
from functions.laplace_filter import apply_laplace_filter

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Read the image for an exercise
image_moon = read_image('../../data/Fig0338(a)(blurry_moon).tif')

# Apply the multistep processing of an image

image_moon_float = toFloat(image_moon)
laplacian_axial = apply_laplace_filter(image_moon_float, type='axial')
laplacian_diagonal = apply_laplace_filter(image_moon_float, type='diagonal')
strength = -1.
image_moon_axial = image_moon_float + strength * laplacian_axial
image_moon_diagonal = image_moon_float + strength * laplacian_diagonal

image_moon_axial_8bit = to8bit(image_moon_axial, mode='truncate')
image_moon_diagonal_8bit = to8bit(image_moon_diagonal, mode='truncate')

plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
plt.imshow(image_moon, cmap='gray', vmin=0, vmax=255)
plt.title('Original blurry image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(to8bit(laplacian_axial), cmap='gray', vmin=0, vmax=255)
plt.title(f'Axial Laplacian of strength {strength}')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(image_moon_axial_8bit, cmap='gray', vmin=0, vmax=255)
plt.title('Sharpened using axial Laplacian')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(image_moon_diagonal_8bit, cmap='gray', vmin=0, vmax=255)
plt.title('Sharpened using diagonal Laplacian')
plt.axis('off')

plt.tight_layout()
plt.show()