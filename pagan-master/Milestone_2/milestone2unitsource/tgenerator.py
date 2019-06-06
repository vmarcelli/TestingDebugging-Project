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
    
    return True

def generator_SHA1(input):
    sha1 = hashlib.sha1()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha1.update(input)
    imgOne = pagan.generator.generate_by_hash(sha1.hexdigest())
    imgTwo = pagan.generator.generate("", 1) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    return True

def generator_SHA224(input):
    sha224 = hashlib.sha224()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha224.update(input)
    imgOne = pagan.generator.generate_by_hash(sha224.hexdigest())
    imgTwo = pagan.generator.generate("", 2) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    return True

def generator_SHA256(input):
    sha256 = hashlib.sha256()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha256.update(input)
    imgOne = pagan.generator.generate_by_hash(sha256.hexdigest())
    imgTwo = pagan.generator.generate("", 3) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    return True

def generator_SHA384(input):
    sha384 = hashlib.sha384()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha384.update(input)
    imgOne = pagan.generator.generate_by_hash(sha384.hexdigest())
    imgTwo = pagan.generator.generate("", 4) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    return True

def generator_SHA512(input):
    sha512 = hashlib.sha512()

    #Update the Hashcode with the input
    #Generate the image using hash
    sha512.update(input)
    imgOne = pagan.generator.generate_by_hash(sha512.hexdigest())
    imgTwo = pagan.generator.generate("", 5) #Default generator is md5
    assert (imgOne is not None)
    assert (imgOne == imgTwo)

    return True


def test_hashGen():
    input = ""
    #Check for version issues
    if(sys.version_info.major == 2):
        input = bytes(input)
    else:
        input = bytes(input, "utf-8")

    assert generator_MD5(input) == True
    assert generator_SHA1(input) == True
    assert generator_SHA224(input) == True
    assert generator_SHA256(input) == True
    assert generator_SHA384(input) == True
    assert generator_SHA512(input) == True

    
