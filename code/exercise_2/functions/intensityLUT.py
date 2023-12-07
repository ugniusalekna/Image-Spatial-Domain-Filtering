import numpy as np

def evalPlt(x, PLT):
    # Check if a given coordinate x is inside the PltInterval instance and interpolate y value
    for interval in PLT:
        if interval.inside(x):
            return interval.eval(x)
        
def intensityLUT(transform, gamma=None, cdf=None, threshold=None, PLT=None):
    # Check the type of transformation requested
    if transform=='powerlaw':
        # Create a lookup table for powerlaw transformation
        lut = np.power(np.arange(0, 256, 1), gamma)
        lut = (255 * (lut - lut.min()) / (lut.max() - lut.min())).astype(np.uint8)
    elif transform=='negation':
        # Create a lookup table for negation transformation
        lut = np.arange(255, -1, -1, dtype=np.uint8)
    elif transform=='equalization':
        # Create a lookup table of possible cdf values for histogram equalization transform
        lut = (255 * cdf).astype(int)
    elif transform=='threshold':
        # Create a lookup table for threshold intensity transformation
        lut = np.where(np.arange(0, 256) >= threshold, 255, 0).astype(np.uint8)
    elif transform=='piecewise_linear':
        lut = np.arange(0, 256, 1).astype(np.uint8)
        # Evaluate the piecewise linear transform for each intensity value and store it in a lookup table
        for value in np.arange(0, 256, 1):
            lut[value] = evalPlt(value, PLT)
    else:
        # If an invalid transformation requested, return empty lookup table
        print('Invalid transformation requested; returning empty lookup table')       
        lut = np.array([], dtype=np.uint8)
    
    return lut