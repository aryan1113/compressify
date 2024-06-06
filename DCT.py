'''
Compute Discrete Cosine Transform of a sub-image matrix
As the human eye is more sensitive to low frequency components, 
we quantize image as such to lose some of the higher frequency components.

Note that computing DCT is not lossy, Quantizing is

1D DCT

2D DCT


Decompose the 2D DCT into two 1D DCT to save on computation
'''