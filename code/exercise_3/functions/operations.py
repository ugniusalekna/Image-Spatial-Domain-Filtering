import numpy as np

def correlation(image, filter):

    # Create a copy of an input image (this will copy the border values to the output image)
    output_image = np.copy(image)
    # Create an empty 2D array same size as the input image (this will leave the border intensity values 0) 
    # output_image = np.zeros_like(image)
    image_width, image_length = image.shape
    filter_width, filter_length = filter.shape

    # Loop through all the pixels of an image
    for i in range(image_width):
        for j in range(image_length):
            # Extract the region of an image that matches the size of a filter
            image_region = image[i:i+filter_width, j:j+filter_length]
            if image_region.shape == filter.shape:
                # Perform correlation by summing elemen-wise multiplication of the region and the filter
                correlation = np.sum(image_region * filter)
                # Store correlation result in the corresponding position of output image    
                output_image[i + (filter_width-1)//2, j + (filter_length-1)//2] = correlation

    return output_image


def convolution(image, filter):
    # Create a copy of an input image (this will copy the border values to the output image)
    output_image = np.copy(image)
    # Create an empty 2D array same size as the input image (this will leave the border intensity values 0) 
    # output_image = np.zeros_like(image)
    image_width, image_length = image.shape
    filter_width, filter_length = filter.shape

    # Rotate the filter manually looping over all the pixels
    # rotated_filter = np.zeros_like(filter)
    # for i in range(filter_width):
    #     for j in range(filter_length):
    #         rotated_filter[i, j] = filter[(filter_width-1) - i, (filter_length-1) - j]

    # Rotate the filter using numpy
    rotated_filter = np.flip(np.flip(filter, axis=0), axis=1)

    # Loop through all the pixels of an input image
    for i in range(image_width):
        for j in range(image_length):
            # Extract the region of an input image matching the size of a filter
            image_region = image[i:i+filter_width, j:j+filter_width]
            if image_region.shape == filter.shape:
                # Perform correlation by summing an element-wise product of rotated filter and the region 
                correlation = np.sum(image_region * rotated_filter)
                # Store the convolution value in the corresponding pixel of an output image
                output_image[i + (filter_width-1)//2, j + (filter_length-1)//2] = correlation

    return output_image
