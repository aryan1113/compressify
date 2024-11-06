from DCT import dct2D
from inverseDCT import idct2D
import unittest
import numpy as np

class TestFrequencyFunctions(unittest.TestCase):
    def setUp(self):
        self.baseCase = [
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
        ]

    def test_dct_idct(self):
        '''
        Round trip should return the same sequence, as effectively we just move 
            from the spatial domain to the frequency domain and the from the 
            frequency domain back to the spatial domain
        '''
        
        input_matrix = self.baseCase
        dct_result = dct2D(input_matrix)
        inverse_dct_result = idct2D(dct_result)

        self.assertTrue(np.allclose(inverse_dct_result, input_matrix))


    def testNormPreservation(self):
        '''
        Norm of a sequence is preserved, i.e. norm remains the same 
            after converting the sequence to frequency domain

        In terms of a matrix, the 1-norm is the maximum of abs column sums
        '''

        input_matrix = self.baseCase
        input_norm = np.linalg.norm(input_matrix)
        dct_result = dct2D(input_matrix)
        dct_norm = np.linalg.norm(dct_result)
        self.assertTrue(input_norm, dct_norm)
        
if __name__ == '__main__':
    unittest.main()