'''
Author: Valerio Marcelli
Date: 4/25/2019
Description:
This is a unit test program for Pagan,
This file in particular uses white box style testing
'''

# Import the pagan module.
import pagan

# Acquire an arbitrary string.
inpt = 'valerio'

def buildWithString(stringOne, stringTwo):
    img = pagan.Avatar(stringOne)
    img2 = pagan.Avatar(stringTwo)
    if(img == img2):
        return True
    else:
        return False

def test_stringInput():
    #True tests
    assert buildWithString("tree", "tree") == True
    assert buildWithString("12345", "12345") == True
    assert buildWithString("voc@b", "voc@b") == True

    #False tests
    assert buildWithString("tree", "apple") == False
    assert buildWithString("12345", "17892") == False
    assert buildWithString("voc@b", "#xtra!") == False


'''

# Use pagan to generate an avatar object based on an input string.
# Optional: You may specify which hash function Pagan should use.
# The functions are available as constants.
# Default: MD5.
img = pagan.Avatar(inpt)

# Open the avatar image in an
# external image viewer.
img.show()

# Set an output path and a file name.
# You don't need to specify a file ending.
# Choose a path depending on your OS.
outpath = 'output/'
filename = inpt

# Saves the avatar image as a .png file
# by omitting the path and name. The
# file endings will be generated automatically.
img.save(outpath, filename)

# You can change the avatar input and
# hash function anytime.
img.change('new input', pagan.SHA256)

'''