# Compressify

Implementing the JPEG file compression scheme
Here's a rough outline of all the process required
<ol>
<li> Convert color space from RGB to Y, Cb, Cr </li>
<li> Subsample the Cb and Cr space </li>
<li> Split image into smaller blocks </li>
<li> Fourier Transform, more precisely Discrete Cosine Transform </li>
<li> Mute higher frequency patterns </li>
<li> Zig Zag scan on resultant matrix </li>
<li> Run Length Encoding </li>
<li> Huffmann Encoding </li>
<li> Calculate Compression Ratio </li>
</ol>

## Size of sub-image ?
Size of sub-image affects transform coding performance. Compression ability and computational complexity increases as sub-image size increases making it a double-edged sword. Most popular sub-image sizes are 8x8 and 16x16

# References
[College of Redwoods](https://www.math.cuhk.edu.hk/~lmlui/dct.pdf)