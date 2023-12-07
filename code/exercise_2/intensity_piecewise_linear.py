import numpy as np
import matplotlib.pyplot as plt
from libtiff import TIFF

from functions.image_io import read_image
from functions.intensityLUT import intensityLUT

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PltInterval:
    # Class variable to store all instances of PltInterval()
    all = []

    def __init__(self, lx, ly, rx, ry):
        # Initialize an instance with x and y coordinates
        self.left_x = lx
        self.left_y = ly
        self.right_x = rx
        self.right_y = ry
        
        # Add the instance to a class list of all instances
        self.all.append(self)
    
    def __repr__(self):
        # Custom string representation of the instance for debugging and display
        return f"PltInterval({self.left_x}, {self.left_y}, {self.right_x}, {self.right_y})"

    def inside(self, x):
        # Check if a given x coordinate is inside the interval
        if self.left_x <= x <= self.right_x:
            return True
        else:
            return False
    
    def eval(self, x):
        # Evaluate a piecewise linear function for the given coordinate x 
        if self.inside(x):
            # Calculate slope and intercept of a linear function
            k = (self.right_y - self.left_y) / (self.right_x - self.left_x)
            b = self.left_y - k * self.left_x
            y = k * x + b
            return y.astype(np.uint8)
    
    @classmethod
    def erase_all(cls):
        # Class method to clear the list of all instances
        cls.all = []

def intensityPLT(image, PLT):
    # Apply the piecewise linear transformation to intensity values of an image using a lookup table
    equalized_image = np.zeros_like(image, dtype=np.uint8)
    lut = intensityLUT(transform='piecewise_linear', PLT=PLT)
    for i in range(256):
        equalized_image[image == i] = lut[i]
    return equalized_image

def plot_piecewise_function(intervals):
    x = np.arange(0, 256, 1).astype(np.uint8)
    y = np.zeros_like(x)

    # For each interval, evaluate the output intensity value of corresponding input values 
    for interval in intervals:
        for i in x:
            if interval.inside(x[i]):
                y[i] = interval.eval(x[i])

    # Plot the piecewise linear function
    plt.plot(x, y)
    plt.axis('square')
    plt.xlabel('Input intensity level $r$')
    plt.ylabel('Output intensity level $s$')
    plt.title('Piecewise linear transformation')
    plt.grid(True)


# Read images for the exercise
image_pollen_dark = read_image('../../data/Fig0316(4)(bottom_left).tif')
image_pollen_light = read_image('../../data/Fig0316(1)(top_left).tif')
image_pollen_medium = read_image('../../data/Fig0316(2)(2nd_from_top).tif')
image_pollen_contrast = read_image('../../data/Fig0316(3)(third_from_top).tif')

# Clear all existing instances of PltInterval (if any)
PltInterval.erase_all()

# Create PltInterval instances to define piecewise linear function
PltInterval(0, 0, 100, 25)
PltInterval(100, 25, 150, 225)
PltInterval(150, 225, 255, 255)

# Add the functions to a list
PLT = PltInterval.all

# Plot the image before and after, and the piecewise linear transformation applied
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(image_pollen_medium, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title('Original image')
plt.subplot(1, 3, 2)
plot_piecewise_function(PLT)
plt.subplot(1, 3, 3)
plt_pollen_medium = intensityPLT(image_pollen_medium, PLT)
plt.imshow(plt_pollen_medium, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.title('Stretched intensity image')
plt.tight_layout()
plt.show()