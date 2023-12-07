import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.intensityLUT import intensityLUT

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def imageNormalize(image):
#     # Normalize pixel values to the range [0, 255] (8 bit range) 
#     return (255 * (image - image.min())/(image.max() - image.min())).astype(np.uint8)

# def intensityPowerlaw(image, gamma):
#     # Create a duplicate of original image
#     duplicate_image = np.copy(image)
#     # Apply the power law
#     duplicate_image = np.power(duplicate_image, gamma)
#     # Scale back to 8 bit range
#     duplicate_image = imageNormalize(duplicate_image)
    
#     return duplicate_image

def intensityPowerlawLUT(image, gamma):
    # Create a duplicate of original image
    duplicate_image = np.copy(image)
    # Create a lookup table for the powerlaw transform
    lut = intensityLUT(transform='powerlaw', gamma=gamma)
    # Apply the power law transform using a lookup table
    duplicate_image = lut[image]

    return duplicate_image

# - - - - - - - - - - - - - - - - - - -
# Applying power law for brightness correction of MRI image
# - - - - - - - - - - - - - - - - - - -

# Load the original image
image_fractured_spine = read_image('../../data/Fig0308(a)(fractured_spine).tif')

# Apply Power Law Transformation to the original image for brightness correction
# A few instances of gamma < 1 are chosen to highlight darker areas
powerlaw_fractured_spine_1 = intensityPowerlawLUT(image_fractured_spine, 0.6)
powerlaw_fractured_spine_2 = intensityPowerlawLUT(image_fractured_spine, 0.4)
powerlaw_fractured_spine_3 = intensityPowerlawLUT(image_fractured_spine, 0.3)

# Create a figure for 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

spine_images = [powerlaw_fractured_spine_1,
                powerlaw_fractured_spine_2,
                powerlaw_fractured_spine_3,
                image_fractured_spine]
spine_titles = ['Power Law: $\gamma = 0.6$',
                'Power Law: $\gamma = 0.4$',
                'Power Law: $\gamma = 0.3$',
                'Original Image']

# Plot each one of the acquired images
for i, ax in enumerate(axs.ravel()):
    ax.imshow(spine_images[i], cmap='gray', vmin=0, vmax=255)
    ax.set_title(spine_titles[i])
    ax.axis('off')

fig.subplots_adjust(
    top=0.945,
    bottom=0.023,
    left=0.012,
    right=0.988,
    hspace=0.127,
    wspace=-0.55)
plt.show()


# - - - - - - - - - - - - - - - - - - -
# Applying power law for removing 'washed-out' appearance
# - - - - - - - - - - - - - - - - - - -

# Load the original image using libtiff
image_aerial = read_image('../../data/Fig0309(a)(washed_out_aerial_image).tif')
# Apply Power Law Transformation to the original image for brightness correction
# A few instances of gamma > 1 are chosen to compress lighter areas
powerlaw_aerial_1 = intensityPowerlawLUT(image_aerial, 3.0)
powerlaw_aerial_2 = intensityPowerlawLUT(image_aerial, 4.0)
powerlaw_aerial_3 = intensityPowerlawLUT(image_aerial, 5.0)

areal_images = [powerlaw_aerial_1,
                powerlaw_aerial_2,
                powerlaw_aerial_3,
                image_aerial]
areal_titles = ['Power Law: $\gamma = 3.0$',
                'Power Law: $\gamma = 4.0$',
                'Power Law: $\gamma = 5.0$',
                'Original Image']

# Create a figure for 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot each one of the acquired images
for i, ax in enumerate(axs.ravel()):
    ax.imshow(areal_images[i], cmap='gray', vmin=0, vmax=255)
    ax.set_title(areal_titles[i])
    ax.axis('off')

fig.subplots_adjust(
    top=0.94,
    bottom=0.024,
    left=0.012,
    right=0.988,
    hspace=0.139,
    wspace=-0.45)
plt.show()
