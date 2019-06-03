'''
Author: Valerio Marcelli
Date: 4/25/2019
Description:
This is a unit test program for Pagan,
This file in particular uses white box style testing
'''

# Import the pagan module.
import pagan

''' 
Image Creation Tests 
'''

def buildWithHash(numOne, numTwo):
    #Create two images with the same string using passed in numbers
    img = pagan.Avatar("", numOne)
    img2 = pagan.Avatar("", numTwo)
    
    #Compate the images using the .img format
    if(img.img == img2.img):
        return True
    else:
        return False

def buildWithString(stringOne, stringTwo):
    #Create two images from the two strings
    img = pagan.Avatar(stringOne)
    img2 = pagan.Avatar(stringTwo)

    #compare the two images (Must use .img format to compare them)
    if(img.img == img2.img):
        return True
    else:
        return False

def test_ImageCreation():
    '''String Tests'''
    #True tests
    assert buildWithString("tree", "tree") == True
    assert buildWithString("12345", "12345") == True
    assert buildWithString("voc@b", "voc@b") == True

    #False tests
    assert buildWithString("tree", "apple") == False
    assert buildWithString("12345", "17892") == False
    assert buildWithString("voc@b", "#xtra!") == False

    '''Hash Tests'''
    #True Tests
    assert buildWithHash(1, 1) == True
    assert buildWithHash(23, 23) == True
    assert buildWithHash(101, 101) == True

    #False Tests
    assert buildWithHash(1, 7) == False
    '''TODO: Fix these two hash tests, perhaps see what they generate'''
    assert buildWithHash(0, 1) == False
    assert buildWithHash(3, 2) == False

    '''Combination Tests'''
    imgTree1 = pagan.Avatar("Tree")
    imgTree2 = pagan.Avatar("Tree", 0)
    imgFalse1 = pagan.Avatar("Tree", 1)
    imgFalse2 = pagan.Avatar("Tree", 3)
    assert imgTree1.img == imgTree2.img
    assert imgFalse1.img != imgFalse2.img

def test_ImageChange():
    '''Change Image Test'''
    #True Tests
    imgOne = pagan.Avatar("1")
    imgZero = pagan.Avatar("0")
    assert imgOne.img != imgZero.img
    imgZero.change("1")
    assert imgZero.img == imgOne.img

    #False Tests
    imgOne = pagan.Avatar("Chicken")
    imgZero = pagan.Avatar("Chicken")
    assert imgOne.img == imgZero.img
    imgZero.change("Egg")
    assert imgZero.img != imgOne.img