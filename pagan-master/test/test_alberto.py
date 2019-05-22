'''
Author: Alberto Valdiviez
Date: 4/25/2019
Description:
This is a unit test program for Pagan,
This file in particular uses white box style testing

this file has the unit test for the hash grinder file
'''

#current update add tests for two functions
# all other tests are blank

import hashgrinder as hg
import generator as gr
from mockito import *
import hashlib


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
def test_hashgrinder_init_weapon_list():
    assert(len(hg.init_weapon_list())==71)


#region Description of hash_input
#takes in an input string, optional (and a hash type)
# returns a hash value
#endregion
def test_generator__hash_input():
    assert(len(gr.hash_input('aaa')) == 64)


def test_grind_hash_fro_aspect():
    assert hg.grind_hash_for_aspect() == 1


def test_hex_to_rgb():
    # invalid input
    assert hg.hex2rgb('#fffff') == 0
    assert hg.hex2rgb('#fffffff') == 0

    # valid input

    assert (255, 255, 255 == hg.hex2rgb('#ffffff'))


def test_grind_hash_for_colors():
    # valid input
    hc = 12
    assert hg.grind_hash_for_colors(hc) == 1


def test_grind_hash_for_weapon():
    hc = 1
    assert hg.grind_hash_for_weapon(hc) == 1


def test_choose_weapon():
    decision = 1
    weapons = 1

    assert hg.choose_weapon(decision, weapons) == 1


def test_choose_aspect():
    decision = 1

    assert hg.choose_aspect(decision) == 1


def test_map_decision():

    digit = 1
    decision = 1

    assert hg.map_decision(digit, decision, digit) == 1


def test_diff():

    a = 1
    b = 2

    assert hg.diff(a, b) == 1
