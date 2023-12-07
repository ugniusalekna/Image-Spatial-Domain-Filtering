import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import show_image

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# - - - - - - - - - - - - - - - -
# Load and visualize different sub-images of SVS file
# - - - - - - - - - - - - - - - -

# tifImg_Kidney2 tif file consists of several sub-images (directories)
tifImg_Kidney2 = TIFF.open('../../data/Kidney2_RGB2_20x.svs')

# By default, directory 0 is read
# To change the directory, we use SetDirectory attribute

# Access tiff file in directory 1 and display it
tifImg_Kidney2.SetDirectory(1)
image_Kidney2_dir1 = TIFF.read_image(tifImg_Kidney2)
show_image(image_Kidney2_dir1)

# Access tiff file in directory 4 and display it
tifImg_Kidney2.SetDirectory(4)
image_Kidney2_dir4 = TIFF.read_image(tifImg_Kidney2)
show_image(image_Kidney2_dir4)

# Access tiff file in directory 5 and display it
tifImg_Kidney2.SetDirectory(5)
image_Kidney2_dir5 = TIFF.read_image(tifImg_Kidney2)
show_image(image_Kidney2_dir5)

tifImg_Kidney2.close()