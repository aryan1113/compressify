import math

def idct2D(input_matrix):
    '''
    Well just plug in values 

    '''
    PI = math.pi
    output_matrix = [[0.0 for _ in range(8)] for _ in range(8)]

    for x in range(8):
        for y in range(8):
            sum_value = 0
            for u in range(8):
                for v in range(8):
                    # apply normalization constants
                    C_u = 1 / math.sqrt(2) if u == 0 else 1
                    C_v = 1 / math.sqrt(2) if v == 0 else 1

                    sum_value += (C_u * C_v *
                                  input_matrix[u][v] *
                                  math.cos(((2.0 * x + 1) * u * PI) / 16.0) *
                                  math.cos(((2.0 * y + 1) * v * PI) / 16.0))
            
            output_matrix[x][y] = round(1 / 4.0 * sum_value, 2)
    return output_matrix
