import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.format_conversion import to8bit
from functions.format_conversion import toFloat
from functions.block_average import apply_block_averaging

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Read the image for an exercise
image_patterns = read_image('../../data/Fig0333(a)(test_pattern_blurring_orig).tif')

# Apply the multistep processing

image_patterns_float = toFloat(image_patterns)

filter_sizes = [3, 5, 9, 15, 25, 35]
blurred_image_list = []
for i in range(len(filter_sizes)):
    image_patterns_blurred = apply_block_averaging(image_patterns_float, filter_size=filter_sizes[i])
    image_patterns_blurred_8bit = to8bit(image_patterns_blurred, mode='minmax')
    blurred_image_list.append(image_patterns_blurred_8bit)

plt.figure(figsize=(14, 9))

for i in range(len(filter_sizes)):
    plt.subplot(2, 3, i+1)
    plt.imshow(blurred_image_list[i], cmap='gray', vmin=0, vmax=255)
    plt.title(f'Squared blur filter of size {filter_sizes[i]}')
    plt.axis('off')
    
plt.tight_layout()
plt.show()