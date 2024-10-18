''' 
Encode information using fewer bits, remove redundancy 
'''

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
    arr = arr.split(",")
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

# sample_arr = "B,B,B,B,B,B,B,B,B,B,G,G,G,G,Y,Y,G,G,L,B,B,B,G"
# print(RLE(sample_arr))

def huffmann(arr):
    pass