import unittest
from collections import Counter
from symbol_encoder import RLE, get_frequency, huffman  

class TestEncodingFunctions(unittest.TestCase):

    def test_RLE(self):
        sample_arr = ['B', 'B', 'B', 'B', 'G', 'G', 'Y', 'Y', 'G']
        expected_output = ["4B", "2G", "2Y", "1G"]
        self.assertEqual(RLE(sample_arr), expected_output)

    def test_get_frequency(self):
        rle_result = ["4B", "2G", "2Y", "2G"]
        expected_freq = Counter({'4B': 1, '2G': 2, '2Y': 1})
        self.assertEqual(get_frequency(rle_result), expected_freq)

    def test_huffman(self):
        rle_result = ["4B", "2G", "2Y", "2G"]
        freq_arr = get_frequency(rle_result)
        encoded_data = huffman(freq_arr, rle_result)
        
        # Check that the encoded data is a string and not empty
        self.assertIsInstance(encoded_data, str)
        self.assertGreater(len(encoded_data), 0)

if __name__ == '__main__':
    unittest.main()
