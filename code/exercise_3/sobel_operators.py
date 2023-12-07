import numpy as np
import matplotlib.pyplot as plt

from functions.image_io import read_image
from functions.format_conversion import to8bit
from functions.format_conversion import toFloat
from functions.sobel_gradients import apply_sobel_gradients

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Read an image for the exercise
image_lens = read_image('../../data/Fig0342(a)(contact_lens_original).tif')

# Apply multistep processing of an image
image_lens_float = toFloat(image_lens)

gradient_magnitude = apply_sobel_gradients(image_lens_float)
gradient_magnitude_8bit = to8bit(gradient_magnitude)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image_lens, cmap='gray', vmin=0, vmax=255)
plt.title('Image of a lens')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gradient_magnitude_8bit, cmap='gray', vmin=0, vmax=255)
plt.title('Sobel gradient magnitude')
plt.axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.show()