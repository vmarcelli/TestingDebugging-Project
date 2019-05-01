'''
Author: Alberto Valdiviez
Date: 4/25/2019
Description:
This is a unit test program for Pagan,
This file in particular uses white box style testing
'''

import pagan

HEX_BASE = 16

def hex2rgb(hexvalue):
    """Converts a given hex color to
    its respective rgb color."""

    # Make sure a possible '#' char is eliminated
    # before processing the color.
    if ('#' in hexvalue):
        hexcolor = hexvalue.replace('#', '')
    else:
        hexcolor = hexvalue

    # Hex colors have a fixed length of 6 characters excluding the '#'
    # TODO: Include custom exception here, even if it should never happen.
    if (len(hexcolor) != 6):
        print ("Unexpected length of hex color value.\nSix characters excluding \'#\' expected.")
        return 0

    # Convert each two characters of
    # the hex to an RGB color value.
    r = int(hexcolor[0:2], HEX_BASE)
    g = int(hexcolor[2:4], HEX_BASE)
    b = int(hexcolor[4:6], HEX_BASE)

    return r, g, b

def test_hex_to_rgb():
    #invalid input
    assert hex2rgb('#fffff') == 0
    assert hex2rgb('#fffffff') == 0

    #valid input

    assert (255, 255, 255 == hex2rgb('#ffffff'))