import numpy as np
from functions.operations import correlation

def generate_average_block(size):
    # Create a 2D array for the average filter filled with ones
    w = np.ones([size, size])
    # Normalize the 2D array by the total number of elements
    w /= size**2
    
    return w


def apply_block_averaging(image, filter_size):
    # Generate an average block filter
    average_filter = generate_average_block(filter_size)
    # Apply correlation to the input image and the generated filter
    output_image = correlation(image, average_filter)
    
    return output_image