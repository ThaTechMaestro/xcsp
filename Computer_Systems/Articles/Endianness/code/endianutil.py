import re

class EndianUtil:
    """
    EndianUtil is a class which carries out reversed byte order operations\n
    This reversals are carried out both ways\n
    Inputs following Big Endian Order are returned\n
        in Little Endian Order & vice versa
    
    Simulating: https://blockchain-academy.hs-mittweida.de/litte-big-endian-converter/
    """ 

    def is_valid_hex(self, val):

        hex_pattern = "^[0-9A-Fa-f]+$"
        return bool(re.match(hex_pattern, val))

    def is_valid_binary(self, val):
      
        binary_pattern = "^[01]+$"
        return bool(re.match(binary_pattern, val))

    def pad_hex_val(self, val):
        """
        Adds leading zeros to hex argument based on some conditions\n
        Also referred to as padding
        
        Example:
            val = a;
            res = pad_hex_val(val);
            res -> 0a;

        Args:
            val (str): hexadecimal value

        Returns:
            str: padded value or passed in hex argument without padding
        """

        pad_val = str(0)
        pad_length = len(val) % 2
        leading_zeros = pad_val * pad_length

        if pad_length != 0:
            return leading_zeros + val

        return val

    def pad_binary_val(self, val):
        """
        Adds leading zeros to binary argument based on some conditions
        Also referred to as padding
        
        Example:
            val = 11;
            res = pad_binary_val(val);
            res -> 0011;

        Args:
            val (str): binary value

        Returns:
            str: padded value or passed in binary argument without padding
        """

        pad_val = str(0)
        pad_length = len(val) % 4
        leading_zeros = pad_val * pad_length

        if pad_length != 0:
            return leading_zeros + val

        return val

    def reverse_hex_endianness(self, val):
        """
        Reverses the endian order of passed in hex argument\n
        Big endian to little endian & vice versa
        
        Example:
            val = abcd;
            res = reverse_hex_endianness(val);
            res -> cdab;

        Args:
            val (str): hex value

        Returns:
            str: reversed byte order of passed in hex argument
        """

        padded_hex_val = self.pad_hex_val(val)
        bytes_data = bytes.fromhex(padded_hex_val)
        reversed_bytes = bytes_data[::-1]

        return reversed_bytes.hex()

    def reverse_bin_endianness(self, val):
        """
        Reverses the endian order of passed in binary argument\n
        Big endian to little endian & vice versa
        
        Example:
            val = 1111111110101010;
            res = reverse_bin_endianness(val);
            res -> 1010101011111111;

        Args:
            val (str): binary value

        Returns:
            str: reversed byte order of passed in binary argument
        """

        padded_bin_val = self.pad_binary_val(val)
        hex_val = hex(int(padded_bin_val, 2))[2:]
        padded_hex_val = self.pad_hex_val(hex_val)
        reversed_endian_hex = self.reverse_hex_endianness(
            self.pad_hex_val(padded_hex_val))

        return bin(int(reversed_endian_hex, 16))[2:]

    def display_reversed_endian_val(self, val):
        """
        Prints reversed endian order of binary/hex argument

        Args:
            val (str): binary or hex value

        Raises:
            ValueError: Empty strings
            ValueError: Invalid hex or binary argument
        """

        if not val:
            raise ValueError("Empty string not allowed")

        if self.is_valid_binary(val):
            padded_binary_val = self.pad_binary_val(val)
            print(self.reverse_bin_endianness(padded_binary_val))
            return

        if self.is_valid_hex(val):
            print(self.reverse_hex_endianness(val))
            return

        raise ValueError("Invalid hex or binary value")


if __name__ == '__main__':

    # Strip for handling leading and trailing whitespaces
    val = str(input('Enter Hex/Binary value: ')).strip().lower()
    endianUtil = EndianUtil()
    endianUtil.display_reversed_endian_val(val)
