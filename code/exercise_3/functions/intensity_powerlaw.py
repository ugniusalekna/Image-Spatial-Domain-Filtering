import numpy as np
from functions.intensityLUT import intensityLUT

def intensityPowerlawLUT(image, gamma):
    # Create a duplicate of original image
    duplicate_image = np.copy(image)
    # Create a lookup table for the powerlaw transform
    lut = intensityLUT(transform='powerlaw', gamma=gamma)
    # Apply the power law transform using a lookup table
    duplicate_image = lut[image]

    return duplicate_image
