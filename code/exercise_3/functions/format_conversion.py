import numpy as np

def toFloat(image): 
    # Convert pixel intensity values to float type
    converted_image = image.astype(float) / 255.0

    return converted_image


def to8bit(image, mode='minmax'):    
    # Min-Max scaling: Scale the image to the full [0, 255] range
    if mode == 'minmax':
        converted_image = (255 * (image - np.min(image)) / (np.max(image) - np.min(image))).astype(np.uint8)
    
    # Truncate mode: Clip values to the [0, 255] range
    if mode == 'truncate':
        converted_image = (255 * np.clip(image, 0, 1)).astype(np.uint8)
    
    return converted_image
