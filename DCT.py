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



Decompose the 2D DCT into two 1D DCT to save on computation
'''
import math

def dct2D(in_matrix):
    PI = math.pi
    out_matrix = [[0.0 for _ in range(8)] for _ in range(8)]

    for u in range(8):
        for v in range(8):
            sum_val = 0
            for x in range(8):
                for y in range(8):
                    sum_val += ( in_matrix[x][y] * 
                                    math.cos(((2.0 * x + 1) * u * PI) / 16.0) * 
                                    math.cos(((2.0 * y + 1) * v * PI) / 16.0)
                                )
            Cu = 1 / math.sqrt(2) if u == 0 else 1
            Cv = 1 / math.sqrt(2) if v == 0 else 1
            
            out_matrix[u][v] = round(1 / 4.0 * Cu * Cv * sum_val, 2)
        return out_matrix


input_matrix = [
[144,	139,	149,	155,	153,	155,    155,	155],
[151,	151,	151,	159,	156,	156,	156,	158],
[151,	156,    160,	162,	159,	151,	151,	151],
[158,	163,    161,	160,	160,	160,	160,	161],
[158,	160,	161,	162,	160,	155,	155,	156],
[161,	161,	161,    161,    160,	157,	157,	157],
[162,	162,	161,	160,	161,	157,	157,	157],
[162	,162,	161,	160,	163,	157,	158,	154]]
print(dct2D(input_matrix))