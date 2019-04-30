import math
## @file GenerateHash.py
#  @title GenerateHash
#  @author Illya Pilipenko
#  @date 2018-10-24


## Amount of colours that are generated from the hash in {@hash_to_colours}
COLOUR_AMOUNT = 8

## Length of a colour in hex
HEX_COLOUR_LEN = 6

## Base of the hexadecimal number system
HEX_BASE = 16

## To generate unique colors, hashes need to
# contain at least this many characters
MINIMUM_COLOUR_HASH_LEN = COLOUR_AMOUNT * HEX_COLOUR_LEN

## Controls debugging mode in this module
DEBUG = False


## @brief Hash To Colours Function
# @details Converts a given string hash value to a set of (r,g,b) tuples. The amount of Color objects is
# determined by the {@COLOUR_AMOUNT} value
# @param hash_value The string from which the colours are generated
# @return a list of (r,g,b) tuples
#
def hash_to_colours(hash_value):
    # if the hash value is smaller than needed to generate the requested amount of colours, the hash value will be
    # continuously added to itself until it is long enough.
    while len(hash_value) < MINIMUM_COLOUR_HASH_LEN:
        missing_hash_length = min(len(hash_value), MINIMUM_COLOUR_HASH_LEN - len(hash_value))
        hash_value += hash_value[:missing_hash_length]

    hash_parts = _split_hash(hash_value, HEX_COLOUR_LEN, COLOUR_AMOUNT)

    colors = []

    for i in range(COLOUR_AMOUNT):
        colors.append(_hex_to_rgb(hash_parts[i]))
    if DEBUG:
        print("Colours: ", colors)
    return colors


## @brief Token Generation Function
# @details Generates a given number of tokens of a given length from a hash value
# @param hash_value The string from which tokens are generated
# @param length The length of each token
# @param amount The amount of tokens to generate
# @throws IndexError Raised if the hash_value parameter is too short to generate the requested tokens
# @return A list of string values of specified length and quantity
def _split_hash(hash_value, length, amount):
    if len(hash_value) < length * amount:
        raise IndexError('hash_value too short to generate requested tokens')
    tokens = []
    for i in range(0, amount):
        tokens.append(hash_value[i*length: (i+1)*length])
    return tokens


## @brief Hex To Colour Tuple Conversion Function
# @details Converts a 6 digit hex colour value into an (r,g,b) tuple
# @param hex_colour The hex value from which a colour is generated
# @return An (r,g,b) tuple
def _hex_to_rgb(hex_colour):
    if DEBUG and len(hex_colour) != HEX_COLOUR_LEN:
        print("Unexpected length of hex color value. \nSix characters excluding \'#\' expected.")
        return 0

    h = hex_colour.lstrip('#')
    rgb = tuple(int(h[i:i + 2], HEX_BASE) for i in (0, 2, 4))
    return rgb


## @brief Hash To Integer Within Given Range
# @details Converts a hash value to an integer between 0 and value_range_size - 1
# @param hash_value The hash value from which to generate an integer
# @param max_value The size of the range within which to generate an integer
# @return An integer between 0 and value_range_size - 1
def hash_to_value_in_range(hash_value, value_range_size):
    required_hash_length = math.ceil(value_range_size / 16.0)
    if len(hash_value) < required_hash_length:
        raise IndexError('hash_value too short to generate integer in requested range')
    i = int(hash_value[:required_hash_length], 16)
    i = i % value_range_size
    return i


# if __name__ == "__main__":
#     hash_val = generate_hash("test")
#     print(hash_val)
#     print(hash_to_colours(hash_val))
#     print(hash_to_colours("0123456789abcdef0123456789abcdef0123456789abcdef"))
#     print(_split_hash("0123456789abcdef", 4, 4))
