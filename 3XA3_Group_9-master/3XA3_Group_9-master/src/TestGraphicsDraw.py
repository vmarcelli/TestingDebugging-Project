import unittest
from graphicsDraw import *
import os
import hashlib
import imghdr


class TestGraphicsDraw(unittest.TestCase):

    def test_image_output_type(self):
        c = generateImage()
        c.generate_and_return_image("output", "Hello", "", "", "", "")
        self.assertEqual(imghdr.what("output.jpg"), 'jpeg')
        c.generate_and_return_image("output1", "123", "", "", "Ghost", "")
        self.assertEqual(imghdr.what("output1.jpg"), 'jpeg')
    def test_output_image_location(self):
        d = generateImage()
        d.generate_and_return_image("test", "Testing", "", "", "", "")
        self.assertEqual(os.getcwd() + "test.jpg", os.path.abspath("test.jpg"))
        
if __name__ == '__main__':
    unittest.main()
