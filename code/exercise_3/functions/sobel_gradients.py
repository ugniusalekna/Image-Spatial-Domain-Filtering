import numpy as np
from functions.operations import convolution


def apply_sobel_gradients(image):
    
    # Define the Sobel kernels for X and Y gradients
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    kernel_y = np.array([[-1, -2, -1],
                         [ 0,  0,  0],
                         [ 1,  2,  1]])

    # Calculate the gradients by convolving an input image with the kernels
    gradient_x = convolution(image, kernel_x)
    gradient_y = convolution(image, kernel_y)

    # Calculate the magnitude of the gradient vector
    # (sum and power operations are computed element-wise) 
    magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    return magnitude