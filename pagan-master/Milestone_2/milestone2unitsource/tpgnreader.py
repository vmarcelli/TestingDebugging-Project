# Author: Alberto Valdiviez
# Date: 4/25/2019
# Description:
# This is a unit test program for Pagan,
# This file in particular uses white box style testing
#
# this file has the unit test for the hash grinder file

from pagan.pgnreader import * 
import os


# region Tests for Pgn Reader
# this test checks function can read the torso.pgn file properly
# given path and filename
def test_parse_pagan_file():
    package = os.path.dirname(os.path.abspath(__file__))
    filename = ('%s%sTORSO.pgn' % (package, os.sep))
    hashcode = '000000123456000000123456000000123456000000000000'
    result = parse_pagan_file(filename, hashcode)
    expected = [(5, 4), (5, 5), (5, 6), (5, 7), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7)]

    assert result == expected


# function should return objects in list every time
# value in hashcode is even, but reading from the end
def test_decide_optional_pixels():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    hashcode = '0101010101'
    result = [(1, 1), (8, 8)]

    assert decideoptionalpixels(pixelmap, hashcode) == result


# Check that given a map of points the return
# x and y will be a vertical mirror from the center
# considering it should fit in 16 by 16 map,
def test_invert_vertical():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    result = [(0, 15), (1, 14), (15, 0), (8, 7)]

    assert invert_vertical(pixelmap) == result


# this function duplicates every point against the vertical center axis
# assuming this will be used for images in 16 by 16 image space
def test_enforce_vertical_symmetry():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    result = [(0, 15), (1, 14), (15, 0), (8, 7), (0, 0), (1, 1), (15, 15), (8, 8)]
    assert enforce_vertical_symmetry(pixelmap) == result


# test subtraction function
def test_diff():
    a = 1
    b = 2

    assert diff(a, b) == 1

    a = -1
    b = -2

    assert diff(a, b) == 1
# endregion
