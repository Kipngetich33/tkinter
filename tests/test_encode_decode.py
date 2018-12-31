# this module contains tests for the encode decode module
from .. encode_decode import encode_decode
import unittest

def fun(x):
    return x + 1

class TestClassEncodeDecode(unittest.TestCase):
    '''
    class that test the functionality of class encode_decode
    with the encode_decode.py module
    '''
    def setUp(self):
        '''
        Function that runs at the begging of each test
        '''
        self.string_to_encode_or_decode = "abcd"

    def test_encode_string(self):
        '''
        Function that test the encode_string function
        '''
        encoded_string = encode_decode(self.string_to_encode_or_decode).encode_string()
        self.assertEqual(encoded_string,"bcde")

    def test_decode_string(self):
        '''
        Function that test the decode_string function
        '''
        encoded_string = encode_decode(self.string_to_encode_or_decode).decode_string()
        self.assertEqual(encoded_string,"zabc")
