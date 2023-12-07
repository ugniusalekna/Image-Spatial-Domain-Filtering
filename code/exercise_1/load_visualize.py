import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.image_io import read_one_tile
from functions.image_io import show_image

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# - - - - - - - - - - - - - - - -
# Load and visualize whole images
# - - - - - - - - - - - - - - - -

image_Kidney1 = read_image('../../data/Kidney1.tif')
show_image(image_Kidney1)
image_Acridine_Or_Gray = read_image('../../data/Region_001_FOV_00041_Acridine_Or_Gray.tif')
show_image(image_Acridine_Or_Gray)
image_DAPI_Gray = read_image('../../data/Region_001_FOV_00041_DAPI_Gray.tif')
show_image(image_DAPI_Gray)
image_FITC_Gray = read_image('../../data/Region_001_FOV_00041_FITC_Gray.tif')
show_image(image_FITC_Gray)
image_SkinOverview = read_image('../../data/SkinOverview.tif')
show_image(image_SkinOverview)
image_TMA2 = read_image('../../data/TMA2-v2.tif')
show_image(image_TMA2)

# - - - - - - - - - - - - - - - -
# Load and visualize sub-rectangle
# - - - - - - - - - - - - - - - -

tile_Kidney1 = read_one_tile('../../data/Kidney1.tif', 240, 0)
show_image(tile_Kidney1)