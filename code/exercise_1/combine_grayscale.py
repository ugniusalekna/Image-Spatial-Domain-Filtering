import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.image_io import show_image
from functions.image_io import write_image

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# - - - - - - - - - - - - - - - -
# Combine grayscale images
# - - - - - - - - - - - - - - - -

# Read grayscale images from TIFF files
image_Acridine_Or_Gray = read_image('../../data/Region_001_FOV_00041_Acridine_Or_Gray.tif')
image_DAPI_Gray = read_image('../../data/Region_001_FOV_00041_DAPI_Gray.tif')
image_FITC_Gray = read_image('../../data/Region_001_FOV_00041_FITC_Gray.tif')

# Get image dimensions
height, width = image_Acridine_Or_Gray.shape

# Create an empty RGB image
combined_RGB_image = np.zeros((height, width, 3), dtype=np.uint8)

# Assign grayscale images to the RGB channels
combined_RGB_image[:, :, 0] = image_Acridine_Or_Gray
combined_RGB_image[:, :, 1] = image_DAPI_Gray
combined_RGB_image[:, :, 2] = image_FITC_Gray

# Display the combined RGB image
show_image(combined_RGB_image)

# Specify the output filename for the combined RGB image
filename_out = '../../output/Region_001_RGB.tif'

# Write the combined RGB image (combined_RGB_image) to the TIFF file
write_image(filename_out, combined_RGB_image)