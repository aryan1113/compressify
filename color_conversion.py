import numpy as np

""" 
Why even change the color space ? 

the human eye is more sensitive to luminance than chrominance, making use of
this property, we can more aggressively  compress the chrominance part without 
any loss in perceptual quality

    Expression for Lumninance (Y) is given by 
        Y = 0.299*R + 0.587*G + 0.114*B
        the human eye is more sensitive to Green > Red > Blue

    Expression for Chrominance Blue (Cb) is given by
        Cb = −0.1687*R − 0.3313*G + 0.5*B + 128
    
    Expression for Chrominance Red (Cr) is given by 
        Cr = 0.5*R − 0.4187*G − 0.0813*B + 128

For calculating Chrominance Blue and Chrominance Red, an offset of +128 is to be added
"""

def rgb_to_ycbcr(image, transformation_matrix = None):
    """
    Convert an RGB image to YCbCr color space.

    image : A 3D numpy array of shape (height, width, 3) representing the RGB image.
    returns : A 3D numpy array of shape (height, width, 3) representing the YCbCr image.
    """

    # Arbitary defined values, based on human percieved values
    transformation_matrix = np.array([
        [ 0.299,  0.587,  0.114],
        [-0.1687, -0.3313,  0.5],
        [ 0.5, -0.4187, -0.0813]
    ])

    # Offset for Cb and Cr components
    offset = np.array([0, 128, 128])

    # Reshape the image to (height * width, 3) for matrix multiplication
    reshaped_image = image.reshape(-1, 3)

    # Apply the transformation
    ycbcr = reshaped_image.dot(transformation_matrix.T) + offset

    # Reshape back to the original image shape
    ycbcr_image = ycbcr.reshape(image.shape)

    return ycbcr_image