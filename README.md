# Compressify

Implementing the JPEG file compression scheme
Here's a rough outline of all the process required
<ol>
<li> Split image into smaller blocks </li>
<li> Convert color space from RGB to Y, Cb, Cr
<li> Subsample the Cb and Cr space
<li> Fourier Transform, more precisely Discrete Cosine Transform </li>
<li> Mute higher frequency patterns
<li> Zig Zag scan on resultant matrix
<li> Run Length Encoding
<li> Huffmann Encoding    
<li> Calculate Compression Ratio