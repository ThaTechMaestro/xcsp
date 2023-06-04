import unittest

from endianutil import EndianUtil


class TestEndianUtil(unittest.TestCase):
    
    def setUp(self):
        self.endian_util = EndianUtil()
    
    def test_is_valid_hex(self):
        
        valid_hex = 'abcd'
        invalid_hex = 'azbg'
        self.assertTrue(self.endian_util.is_valid_hex(valid_hex))
        self.assertFalse(self.endian_util.is_valid_hex(invalid_hex))
    
    def test_is_valid_binary(self):
        
        valid_bin = '010111'
        invalid_bin = 'abcd'
        self.assertTrue(self.endian_util.is_valid_binary(valid_bin))
        self.assertFalse(self.endian_util.is_valid_binary(invalid_bin))
    
    def test_pad_hex_val(self):
        
        self.assertEqual(self.endian_util.pad_hex_val('a'),'0a')
        self.assertEqual(self.endian_util.pad_hex_val('ab'),'ab')
        self.assertEqual(self.endian_util.pad_hex_val('abc'),'0abc')  
        self.assertEqual(self.endian_util.pad_hex_val('abcd'),'abcd')

    def test_pad_binary_val(self):
        
        self.assertEqual(self.endian_util.pad_binary_val('01'),'0001')
        self.assertEqual(self.endian_util.pad_binary_val('1011'),'1011')
        self.assertEqual(self.endian_util.pad_binary_val('101111'),'00101111')  
        self.assertEqual(self.endian_util.pad_binary_val('11110001'),'11110001')
    
    def test_reverse_hex_endianness(self):
        
        self.assertEqual(self.endian_util.reverse_hex_endianness('a'), '0a')
        self.assertEqual(self.endian_util.reverse_hex_endianness('abc'), 'bc0a')
        self.assertEqual(self.endian_util.reverse_hex_endianness('abcd'), 'cdab')
    
    def test_reverse_bin_endianness(self):
        
        self.assertEqual(self.endian_util.reverse_bin_endianness('1011'), '1011')
        self.assertEqual(self.endian_util.reverse_bin_endianness('101110'), '101110')
        self.assertEqual(self.endian_util.reverse_bin_endianness('101110111'), '111011100000001')
        self.assertEqual(self.endian_util.reverse_bin_endianness('1111101011110101'), '1111010111111010')
    
    
    def test_display_reversed_endian_val_raises_exception_for_invalid_input(self):
        
        with self.assertRaises(ValueError) as e:
            self.endian_util.display_reversed_endian_val('')
        self.assertEqual(str(e.exception), 'Empty string not allowed')
        with self.assertRaises(ValueError) as e:    
            self.endian_util.display_reversed_endian_val('   ')
        self.assertEqual(str(e.exception), 'Invalid hex or binary value')
        with self.assertRaises(ValueError) as e:    
            self.endian_util.display_reversed_endian_val('zzzzzz')
        self.assertEqual(str(e.exception), 'Invalid hex or binary value')
        with self.assertRaises(ValueError) as e:    
            self.endian_util.display_reversed_endian_val('-10101')
        self.assertEqual(str(e.exception), 'Invalid hex or binary value')
    
    
if __name__ == '__main__':
    unittest.main()