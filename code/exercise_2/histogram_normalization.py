import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.intensityLUT import intensityLUT

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_intensity_count(image):
    
    # Store the count of each intensity value [0-255] of an image
    histogram = np.zeros(256).astype(int)
    for pixel_intensity in image.flatten():
        histogram[pixel_intensity] += 1
    return histogram

def plot_histogram(image):

    histogram = get_intensity_count(image)
    # image_name = get_variable_name(image)
    plt.bar(np.arange(0, 256, 1, dtype=np.uint8), histogram, width=1.0)
    # plt.title(f'Intensity Value Histogram of {image_name}')
    plt.title('Histogram')
    plt.xlabel('Intensity Values')
    plt.ylabel('Frequency')
    plt.grid(axis='y')

def calculate_pdf(image):
    histogram = get_intensity_count(image)
    pdf = histogram / len(image.flatten())
    return pdf

def calculate_cdf(pdf):
    cdf = np.zeros(256)
    for i in range(256):
        cdf[i] = np.sum(pdf[: i])
    return cdf

def histogram_equalization(image):
    
    # Calculate probability density function from histogram of input image 
    pdf = calculate_pdf(image)
    
    # Calculate cumulative distribution function
    cdf = calculate_cdf(pdf)
    
    # Calculate histogram normalizing intensity transform
    equalized_image = np.zeros_like(image, dtype=np.uint8)
    # Use cdf intensity values from the lookup table 
    cdf_lut = intensityLUT(transform='equalization', cdf=cdf)

    for i in range(256):
        equalized_image[image == i] = cdf_lut[i]

    return equalized_image
    
def get_variable_name(variable):
    for name in globals():
        if id(globals()[name]) == id(variable):
            return name
    for name in locals():
        if id(locals()[name]) == id(variable):
            return name
    return None

def plot_image_hist(image, image_equalized, m, n, i):
    
    plt.subplot(m, n, n*i+1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title(get_variable_name(image))

    plt.subplot(m, n, n*i+2)
    plot_histogram(image)

    plt.subplot(m, n, n*i+3)
    plt.imshow(image_equalized, cmap='gray', vmin=0, vmax=255)
    plt.title(get_variable_name(image) + ' equalized')

    plt.subplot(m, n, n*i+4)
    plot_histogram(image_equalized)


# Read images for the exercise
image_pollen_dark = read_image('../../data/Fig0316(4)(bottom_left).tif')
image_pollen_light = read_image('../../data/Fig0316(1)(top_left).tif')
image_pollen_medium = read_image('../../data/Fig0316(2)(2nd_from_top).tif')
image_pollen_contrast = read_image('../../data/Fig0316(3)(third_from_top).tif')

# Create a figure for the plots and histograms
plt.figure(figsize=(12, 12))

# Acquire images and equalized images
images = [
    image_pollen_dark,
    image_pollen_light,
    image_pollen_medium,
    image_pollen_contrast
]
equalized_images = [
    histogram_equalization(image_pollen_dark),
    histogram_equalization(image_pollen_light),
    histogram_equalization(image_pollen_medium),
    histogram_equalization(image_pollen_contrast)
]

# Plot each one of the acquired images and the histograms corresponding to the images
for i in range(4):
    plot_image_hist(images[i], equalized_images[i], 4, 4, i)

# plt.tight_layout()
plt.subplots_adjust(
    top=0.961,
    bottom=0.069,
    left=0.0,
    right=0.997,
    hspace=0.75,
    wspace=0.01
)

plt.show()