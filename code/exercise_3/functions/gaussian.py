import numpy as np
from functions.operations import correlation


def generate_gaussian(size, sigma=1.):
    # Create empty 2D array for gaussian filter
    w = np.zeros([size, size])

    # Genetate a linear space of values centered at (0, 0)
    linspace = np.linspace(-(size - 1) / 2, (size - 1) / 2, size, dtype=np.int8)

    if (size % 2 != 0):
        # Calculate the gaussian values for each position in the filter
        for x in linspace:
            for y in linspace:
                w[x + (size-1)//2, y + (size-1)//2] = np.exp(-(x**2 + y**2) / (2. * sigma**2))

        # Normalize the filter
        w /= np.sum(w)

    else:
        print('Filter size should be an odd integer')

    return w


def apply_gaussian_filter(image, filter_size, sigma=1.):
    # Generate gaussian filter
    gaussian_filter = generate_gaussian(filter_size, sigma)
    # Apply correlation to the input image and the generated filter
    output_image = correlation(image, gaussian_filter)
    
    return output_image