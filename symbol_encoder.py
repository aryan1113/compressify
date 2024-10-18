''' 
Encode information using fewer bits, remove redundancy 
'''
from collections import Counter
import heapq

def RLE(arr):
    '''
    RLE : Run Length Encoding

    Input  : flattened matrix (or array)
    Output : intensity values mapped with their runs

    Example :
    input_arr = B,B,B,B,B,B,B,B,B,B,G,G,G,G,Y,Y,G,G
    encoded_arr = 10B,4G,2Y,2G

    More info : 
    compresses consecutive occurences of a symbol with only one copy, along with its count
    '''

    # change the splitting criterion as per input scheme
    # arr = arr.split(",")
    arr_len = len(arr)
    encoded_arr = []
    
    count = 1

    for element in range(1, arr_len):

        # avoid repeated calculations for symbols
        if arr[element]==arr[element-1]:
            count +=1

        else:
            encoded_arr.append(f"{count}{arr[element - 1]}")
            count = 1
    encoded_arr.append(f"{count}{arr[-1]}")
    return encoded_arr


# sample_arr = ['B','B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'G', 'G', 'G', 'G', 'Y', 'Y', 'G', 'G']
# encoded_rle = RLE(sample_arr)
# print(encoded_rle)  # Output: "10B,4G,2Y,2G"

def get_frequency(arr):
    return Counter(arr)

def huffman(freq_arr, rle_result):
    
    # Create a heap from the frequency table (for the RLE encoded strings)
    heap = [ [weight, [symbol, ""]] for symbol, weight in freq_arr.items() ]
    # creates a min heap
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(
                        heap, 
                        [ lo[0] + hi[0] ] + lo[1:] + hi[1:]
                        )

    
    huff_dict = {symbol: code for symbol, code in heap[0][1:]}
    

    # Encode the RLE result using the Huffman dictionary into a bitstream
    encoded_data = "".join([huff_dict[symbol] for symbol in rle_result])
    return encoded_data

# drive code
if __name__ == "__main__":
    sample_arr = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'G', 'G', 'G', 'G', 'Y', 'Y', 'G', 'G']
    encoded_rle = RLE(sample_arr)
    print("RLE Encoded:", encoded_rle)  # Output: ['10B', '4G', '2Y', '2G']

    # Get frequency of RLE encoded symbols
    rle_freq = get_frequency(encoded_rle)
    print("Frequency Table:", rle_freq)

    
    encoded_data = huffman(rle_freq, encoded_rle)
    print("Huffman Encoded Data:", encoded_data)
