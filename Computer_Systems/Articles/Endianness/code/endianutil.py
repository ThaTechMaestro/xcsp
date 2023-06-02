# https://blockchain-academy.hs-mittweida.de/litte-big-endian-converter/
import re


class EndianUtil:

    '''
    '''

    def is_valid_hex(self, val):

        hex_pattern = "^[0-9A-Fa-f]+$"
        return bool(re.match(hex_pattern, val))

    def is_valid_binary(self, val):

        binary_pattern = "^[01]+$"
        return bool(re.match(binary_pattern, val))

    def pad_hex_val(self, val):

        pad_val = str(0)
        pad_length = len(val) % 2
        leading_zeros = pad_val * pad_length

        if pad_length != 0:
            return leading_zeros + val

        return val

    def pad_binary_val(self, val):

        pad_val = str(0)
        pad_length = len(val) % 4
        leading_zeros = pad_val * pad_length

        if pad_length != 0:
            return leading_zeros + val

        return val

    def reverse_hex_endianness(self, val):

        padded_hex_val = self.pad_hex_val(val)
        bytes_data = bytes.fromhex(padded_hex_val)
        reversed_bytes = bytes_data[::-1]

        return reversed_bytes.hex()

    def reverse_bin_endianness(self, val):

        padded_bin_val = self.pad_binary_val(val)
        hex_val = hex(int(padded_bin_val, 2))[2:]
        padded_hex_val = self.pad_hex_val(hex_val)
        reversed_endian_hex = self.reverse_hex_endianness(
            self.pad_hex_val(padded_hex_val))

        return bin(int(reversed_endian_hex, 16))[2:]

    def display_reversed_endian_val(self, val):

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
    # print(a.display_reversed_endian_val("0101"))
