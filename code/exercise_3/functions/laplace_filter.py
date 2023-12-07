import numpy as np
from functions.operations import convolution

def apply_laplace_filter(image, type='axial'):
    # Create laplace filter
    if type == 'axial':
        laplace_filter = np.array([[0,  1, 0],
                                   [1, -4, 1],
                                   [0,  1, 0]])
    
    elif type == 'diagonal':
        laplace_filter = np.array([[1,  1, 1],
                                   [1, -8, 1],
                                   [1,  1, 1]])

    else: print('Laplace filter type not valid!')
    
    # Convolve the input image with a created filter; the strength of sharpening
    #  filter can be adjusted
    laplacian = convolution(image, laplace_filter)
    
    # Since the filter is not normalized, the output
    # needs to be scaled down to [0, 255] for further use
    
    return laplacian