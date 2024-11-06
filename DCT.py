import numpy as np
'''
Compute Discrete Cosine Transform of a sub-image matrix
As the human eye is more sensitive to low frequency components, 
we quantize image as such to lose some of the higher frequency components.

Note that computing DCT is not lossy, Quantizing is

1D DCT
For a signal x = [x1,x2,x3,x4.....,x_N] having N samples, the k_th DCT coeff is given as 

O(n^2) impractical approach =>
c_k = 0
for n in range(0, N-1):
    ck += 2 * (
         x_n * cos( 
            math.pi*k * ( 
                (2 * n) + 1 
                    ) 
                    / (2 * N ) 
            ) 
         )

C_u is a normalization constant (as is C_v), that have value = 1/sqrt(2) u == 0, else 1
'''
import math

def dct2D(input_matrix):
    '''
    Calculates the 2D Discrete Cosine Transform of a matrix

    Args: 
        input_matrix : the matrix to be transformed

    Returns:
        the 2D Cosine Transform of the matrix
    '''
    PI = math.pi
    output_matrix = [[0.0 for _ in range(8)] for _ in range(8)]

    for u in range(8):
        for v in range(8):
            sum_value = 0
            for x in range(8):
                for y in range(8):
                    sum_value += ( input_matrix[x][y] * 
                                    math.cos(((2.0 * x + 1) * u * PI) / 16.0) * 
                                    math.cos(((2.0 * y + 1) * v * PI) / 16.0)
                                )
                            
            # apply normalization constants
            C_u = 1 / math.sqrt(2) if u == 0 else 1
            C_v = 1 / math.sqrt(2) if v == 0 else 1
            
            output_matrix[u][v] = round(1 / 4.0 * C_u * C_v * sum_value, 2)
    return output_matrix


def fft1D(sequence):
    N = len(sequence)
    if N <= 1:
        return sequence

    # FFT for even indexed elements
    even = fft1D(sequence[0::2])

    # FFT for odd indexed elements
    odd = fft1D(sequence[1::2])  

    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def fft2D(input_matrix):
    rows_fft = [ fft1D(row) for row in input_matrix ]
    cols_fft = [fft1D(col) for col in np.array(rows_fft).T]
    
    magnitude = np.array(cols_fft).T
    return magnitude

# trash code, to test stuff
# later can be moved to a separate testing file

# input_matrix = [
# [144,	139,	149,	155,	153,	155,    155,	155],
# [151,	151,	151,	159,	156,	156,	156,	158],
# [151,	156,    160,	162,	159,	151,	151,	151],
# [158,	163,    161,	160,	160,	160,	160,	161],
# [158,	160,	161,	162,	160,	155,	155,	156],
# [161,	161,	161,    161,    160,	157,	157,	157],
# [162,	162,	161,	160,	161,	157,	157,	157],
# [162	,162,	161,	160,	163,	157,	158,	154]]

# np.set_printoptions(suppress=True)

# # built in library under numyp
# print("NumPy FFT Result:")
# np_fft_result = np.fft.fft2(input_matrix)
# np_magnitude = np.abs(np_fft_result)
# np_magnitude = np.round(np_magnitude, 3)

# print(np_magnitude)

# print()

# print("Our FFT Implementation Results are: ")
# our_implementation = np.abs(fft2D(input_matrix))
# our_implementation= np.round(our_implementation, 3)
# print(our_implementation)

# print(np_fft_result == our_implementation)



# '''
# Compare DCT and fFT results

# FFT results seem a bit too large, this might negatively affect the quantization process
# but this is something we can afford over a large computation improvement
# '''
# print("FFT results from our implemenation are :")
# print(np_magnitude)

# dct_implementation = np.round( dct2D(input_matrix), 3)
# print("DCT results from our implementation are: ")
# print(dct_implementation)
# print(np_magnitude == dct_implementation)