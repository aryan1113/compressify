'''
8x8 matrix
(0,0) is the DC component of the block, will be quantized with a factor of 16
'''
default_normalization = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99],
                        ]

def dead_zone_quantizer(input_matrix, normalize_matrix = default_normalization):
    
    '''
    input_matrix should be a 8x8 grid
    '''
    
    rows, cols = len(input_matrix), len(input_matrix[0])
    output_matrix = [ [0]*rows ] * cols

    for row in range(rows):
        for col in range(cols):
            output_matrix[row][col] = round(input_matrix[row][col]/normalize_matrix[row][col])
    return output_matrix

def zig_zag_scan(input_matrix):
    """
    computes the zigzag of a quantized block
    input_matrix : quantized matrix
    returns: zigzag vectors in an array
    """

    # initializing the variables
    h, v = 0, 0

    v_min, h_min = 0, 0

    v_max, h_max = len(input_matrix), len(input_matrix[0])

    i = 0
    scan_string = [0]*( (v_max * h_max) )
    print('ini', scan_string)

    while (v < v_max) and (h < h_max):

        if ((h + v) % 2) == 1:  # going up
            if v == v_min:
                scan_string[i] = input_matrix[v][h]  # first line
                if h == h_max:
                    v = v + 1
                else:
                    h = h + 1
              

            elif (h == h_max - 1) and (v < v_max):  # last column
                scan_string[i] = input_matrix[v][h]
                v = v + 1
              
            elif (v > v_min) and (h < h_max - 1):  # all other cases
                scan_string[i] = input_matrix[v][h]
                v = v - 1
                h = h + 1
               

        else:  # going down
            if (v == v_max - 1) and (h <= h_max - 1):  # last line
                scan_string[i] = input_matrix[v][h]
                h = h + 1
                
            elif h == h_min:  # first column
                scan_string[i] = input_matrix[v][h]
                if v == v_max - 1:
                    h = h + 1
                else:
                    v = v + 1
               
            elif (v < v_max - 1) and (h > h_min):  # all other cases
                scan_string[i] = input_matrix[v][h]
                v = v + 1
                h = h - 1
                
        i+=1
  
        if (v == v_max - 1) and (h == h_max - 1):  # bottom right element
            scan_string[i] = input_matrix[v][h]
            break
    
    return scan_string


test_mat = [
       [ 0,  1,  5],
       [12, 14, 54],
       [32, 43, 11]
       ]
print(zig_zag_scan(test_mat))