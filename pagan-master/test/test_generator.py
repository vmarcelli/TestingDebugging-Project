'''                              
 UNLESS YOUR NAME IS VALERIO DO NOT TOUCH THIS CODE
'''
import pagan
import pytest
import sys
import os
import hashlib


def generator_MD5(input):
    md5 = hashlib.md5()

    #Update the Hashcode with the input
    #Generate the image using hash
    md5.update(input)
    imgOne = pagan.generator.generate_by_hash(md5.hexdigest())
    imgTwo = pagan.generator.generate("", 0) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    #Pytest Errors
    with pytest.raises(pagan.generator.FalseHashError):
        imgOne = pagan.generator.generate_by_hash(md5.hexdigest()[:2])
    with pytest.raises(pagan.generator.FalseHashError):
        imgOne = pagan.generator.generate_by_hash(md5.hexdigest()+"A")

def generator_SHA1(input):
    sha1 = hashlib.sha1()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha1.update(input)
    imgOne = pagan.generator.generate_by_hash(sha1.hexdigest())
    imgTwo = pagan.generator.generate("", 1) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

def test_hashGen():
    input = ""
    #Check for version issues
    if(sys.version_info.major == 2):
        input = bytes(input)
    else:
        input = bytes(input, "utf-8")

    generator_MD5(input)
    generator_SHA1(input)

    
