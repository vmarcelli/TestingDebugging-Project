# Author: Alberto Valdiviez
# Date: 4/25/2019
# Description:
# This is a unit test program for Pagan,
# This file in particular uses white box style testing
#
# this file has the unit test for the hash grinder file


# current update add tests for two functions
# all other tests are blank

from pagan.hashgrinder import * 

import os

# region Tests for Hashgrinder
# region Return of init_weapon_list
# 10 [['GREATSWORD'], ['BIGHAMMER'], ['GREATMACE'], ['GREATAXE'], ['WAND'], ['SWORD'], ['HAMMER'], ['AXE'], ['FLAIL'], ['MACE'],
# 10 ['DAGGER'], ['SWORD', 'SWORD'], ['SWORD', 'HAMMER'], ['SWORD', 'AXE'], ['SWORD', 'FLAIL'], ['SWORD', 'MACE'], ['SWORD', 'DAGGER'], ['HAMMER', 'SWORD'], ['HAMMER', 'HAMMER'], ['HAMMER', 'AXE'],
# 10 ['HAMMER', 'FLAIL'], ['HAMMER', 'MACE'],['HAMMER', 'DAGGER'], ['AXE', 'SWORD'], ['AXE', 'HAMMER'], ['AXE', 'AXE'], ['AXE', 'FLAIL'], ['AXE', 'MACE'], ['AXE', 'DAGGER'],  ['FLAIL', 'SWORD'],
# 10 ['FLAIL', 'HAMMER'], ['FLAIL', 'AXE'], ['FLAIL', 'FLAIL'], ['FLAIL', 'MACE'], ['FLAIL', 'DAGGER'], ['MACE', 'SWORD'], ['MACE', 'HAMMER'], ['MACE', 'AXE'], ['MACE', 'FLAIL'], ['MACE', 'MACE'],
# 10 ['MACE', 'DAGGER'], ['DAGGER', 'SWORD'], ['DAGGER', 'HAMMER'], ['DAGGER', 'AXE'], ['DAGGER', 'FLAIL'], ['DAGGER', 'MACE'], ['DAGGER', 'DAGGER'], ['LONGSHIELD', 'SWORD'], ['ROUNDSHIELD', 'SWORD'],['BUCKLER', 'SWORD'],
# 4     ['SHIELD', 'SWORD'], ['LONGSHIELD', 'HAMMER'], ['ROUNDSHIELD', 'HAMMER'], ['BUCKLER', 'HAMMER'],
# 6     ['SHIELD', 'HAMMER'], ['LONGSHIELD', 'AXE'], ['ROUNDSHIELD', 'AXE'], ['BUCKLER', 'AXE'], ['SHIELD', 'AXE'], ['LONGSHIELD', 'FLAIL'],
# 6     ['ROUNDSHIELD', 'FLAIL'], ['BUCKLER', 'FLAIL'], ['SHIELD', 'FLAIL'], ['LONGSHIELD', 'MACE'], ['ROUNDSHIELD', 'MACE'], ['BUCKLER', 'MACE'],
# 5     ['SHIELD', 'MACE'], ['LONGSHIELD', 'DAGGER'], ['ROUNDSHIELD', 'DAGGER'], ['BUCKLER', 'DAGGER'], ['SHIELD', 'DAGGER']]
# endregion


# checks the number of values in the result of init weapon list
# the result should always be equal to the contents above
def test_hashgrinder_init_weapon_list():
    assert(len(init_weapon_list()) == 71)


# region Description of Grind hash
# what does this piece of code do
# endregion

# this test that the return of grind hash aspect
# is the same as as running the choose aspect function
# wrapped around map decision function
def test_grind_hash_for_aspect():
    max = 16777215
    aspect = 16
    hc = '123456'
    last = int(hc, 16)
    assert grind_hash_for_aspect(hc) == choose_aspect(map_decision(max, aspect, last))
    hc = 'af234b'
    last = int(hc, 16)
    assert grind_hash_for_aspect(hc) == choose_aspect(map_decision(max, aspect, last))


# this checks that hex2rgb properly converts a
# hexadecimal color to three rgb values
# or a zero if not a valid hex number
def test_hex_to_rgb():
    # invalid input
    assert hex2rgb('#fffff') == 0
    assert hex2rgb('#fffffff') == 0

    # valid input
    assert hex2rgb('#000000') == (0, 0, 0)
    assert hex2rgb('#888888') == (136, 136, 136)
    assert hex2rgb('#ffffff') == (255, 255, 255)


# this test the grind hash colors
# this results in 8 colors
# test checks that the size of input
# and checks for valid output
def test_grind_hash_for_colors():
    # valid input
    hc_min = '000000123456000000123456000000123456000000123456'
    hc_max = '000000123456000000123456000000123456000000123456000123'
    hc_less_min = '000000123456000000123456000000123456'
    hc_white = '000000'
    hc_black = 'ffffff'

    assert len(grind_hash_for_colors(hc_min)) == 8
    assert len(grind_hash_for_colors(hc_max)) == 8
    assert len(grind_hash_for_colors(hc_less_min)) == 8
    assert grind_hash_for_colors(hc_white)[0] == (0, 0, 0,)
    assert grind_hash_for_colors(hc_black)[7] == (255, 255, 255)


# checks the input against the output
# to make sure it returns the proper result as determined
# by the output of the wrapped functions
def test_grind_hash_for_weapon():
    hc = '000000123456'
    hc2 = '000000abcdef'
    max = 16777215
    wlist = init_weapon_list()
    len_weapon_list = len(wlist)
    last = int(hc, 16)
    last2 = int(hc2,16)

    assert grind_hash_for_weapon(hc) == choose_weapon(map_decision(max, len_weapon_list, last), wlist)
    assert grind_hash_for_weapon(hc2) == choose_weapon(map_decision(max, len_weapon_list, last2), wlist)


# test choose weapon function
# given input of a list, it should return
# the value of the list at position decision-1
def test_choose_weapon():

    decision = 7
    #list of weapons
    weapons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert choose_weapon(decision, weapons) == weapons[decision-1]

    decision = 6
    assert choose_weapon(decision, weapons) == weapons[decision - 1]
    decision = 8
    assert choose_weapon(decision, weapons) == weapons[decision - 1]


# returns a list aspect options from hashgrinder file
def test_choose_aspect():

    assert choose_aspect(0) == []
    assert choose_aspect(1) == ['HAIR']
    assert choose_aspect(7) == ['HAIR', 'PANTS', 'BOOTS']
    assert choose_aspect(16) == []
    assert choose_aspect(17) == []


# this functions result should match function given input
# using the algorithm to make a decision
def test_map_decision():

    a = 1
    b = 1
    c = 1

    assert map_decision(a, b, c) == (b / (float(a) + 1)) * (float(c) + 1)

    a = 4
    b = 9
    c = 10

    assert map_decision(a, b, c) == (b / (float(a) + 1)) * (float(c) + 1)


# checks that the function properly splits a sequence into chunks
def test_split_sequence():
    sequence = 'abcdefghijklmnopqrstuvwx'

    result_8 = split_sequence(sequence, 3)
    result_2 = split_sequence(sequence, 2)
    result_12 = split_sequence(sequence, 12)
    assert len(result_8) == 8
    assert len(result_2) == 12
    assert len(result_12) == 2


# takes difference
def test_diff():

    a = 1
    b = 2

    assert diff(a, b) == 1

    a = -1
    b = -2

    assert diff(a, b) == 1
# endregion
