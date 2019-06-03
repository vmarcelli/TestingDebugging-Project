import pagan
import pytest
import sys
import os

def generator_MD5():
    print()

def test_hashGen():
    import hashlib
    md5 = hashlib.md5()
    input = ""

    #Check for version issues
    if(sys.version_info.major == 2):
        input = bytes(input)
    else:
        input = bytes(input, "utf-8")

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

    #Test Globals
    assert pagan.generator.OUTPUT_PATH == ('%s%soutput%s' % (os.getcwd(), os.sep, os.sep))
