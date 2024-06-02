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

def RLE(arr):
    # change the splitting criterion as per input scheme
    arr = arr.split(",")
    arr_len = len(arr)
    encoded_arr = ""
    
    count = 1
    just_processed = ""

    for element in range(arr_len-1):
        count = 1
        
        # avoid repeated calculations for symbols
        if just_processed==arr[element]:
            pass

        else:

            while element != arr_len-1 and ( arr[element] == arr[element+1] ):
                count+=1
                element+=1
                just_processed = arr[element]

        
            encoded_arr+=str(count)+ arr[element]+ ","

    encoded_arr = encoded_arr[:-1]
    return encoded_arr

# sample_arr = "B,B,B,B,B,B,B,B,B,B,G,G,G,G,Y,Y,G,G"
# print(RLE(sample_arr))

'''
To run this file use 
python RLE.py 
'''