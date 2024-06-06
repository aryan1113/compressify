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

def dct(frame, orthonormal = True):
    N = len(frame)
    out = np.zeros_like(frame)
    for k in range(N):
        for (n, xn) in enumerate(frame):
            out[k] += xn * np.cos(np.pi * k * (2 * n + 1) / (2 * N))
        scale = np.sqrt(1 / (4 * N)) if k == 0 else np.sqrt(1 / (2 * N))
        out[k] *= 2 * scale if orthonormal else 2
    return out
