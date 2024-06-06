'''
Intends to 
1. Convert color space from RGB to Y, Cb, Cr
2. Subsample the Cb and Cr space 
3. Split image into smaller blocks
'''
import numpy as np
import cv2

def split_image(image,kernel_size):
    #compute squares that will be created
    pass

def convert_color_space(image, resize_height = 480, resize_width = 480):
    RGB_image = cv2.imread(image)
    RGB_image = cv2.resize(RGB_image, (resize_height, resize_width))

    YCrCbImage = cv2.cvtColor(BGRImage, cv2.COLOR_BGR2YCR_CB)

    Y, Cb, Cr = ( YCrCbImage[:,:,0], 
                YCrCbImage[:,:,1], 
                YCrCbImage[:,:,2] )

    Y, Cb, Cr = ( 
        np.array(Y).astype(np.int16), 
        np.array(Cb).astype(np.int16), 
        np.array(Cr).astype(np.int16) 
                  )
    # change scale
    Y -= 128
    Cb -= 128
    Cr -= 128
    pass

    # compress domain space alag se


'''

'''