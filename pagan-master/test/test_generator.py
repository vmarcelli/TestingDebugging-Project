import pagan
import pytest
import sys
import os

def test_hashGen():
    import pagan
    md5 = hashlib.md5()

    #Test Globals
    assert pagan.generator.OUTPUT_PATH == ('%s%soutput%s' % (os.getcwd(), os.sep, os.sep))
