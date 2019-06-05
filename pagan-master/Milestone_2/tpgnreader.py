# Author: Alberto Valdiviez
# Date: 4/25/2019
# Description:
# This is a unit test program for Pagan,
# This file in particular uses white box style testing
#
# this file has the unit test for the hash grinder file

import pagan.pgnreader as pr
import os

# region Tests for Pgn Reader
def test_parse_pagan_file():
    package = os.path.dirname(os.path.abspath(__file__))
    filename = ('%s%sTORSO.pgn' % (package, os.sep))
    hashcode = '000000123456000000123456000000123456000000000000'
    result = pr.parse_pagan_file(filename, hashcode)
    expected = [(5, 4), (5, 5), (5, 6), (5, 7), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7)]

    assert result == expected


def test_decide_optional_pixels():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    hashcode = '0101010101'
    result = [(1, 1), (8, 8)]

    assert pr.decideoptionalpixels(pixelmap, hashcode) == result


def test_invert_vertical():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    result = [(0, 15), (1, 14), (15, 0), (8, 7)]

    assert pr.invert_vertical(pixelmap) == result


def test_enforce_vertical_symmetry():
    pixelmap = [(0, 0), (1, 1), (15, 15), (8, 8)]
    result = [(0, 15), (1, 14), (15, 0), (8, 7), (0, 0), (1, 1), (15, 15), (8, 8)]
    assert pr.enforce_vertical_symmetry(pixelmap) == result


def test_diff():
    a = 1
    b = 2

    assert pr.diff(a, b) == 1

    a = -1
    b = -2

    assert pr.diff(a, b) == 1
# endregion
