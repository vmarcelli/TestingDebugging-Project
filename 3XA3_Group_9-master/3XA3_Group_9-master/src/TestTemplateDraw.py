import unittest
from TemplateDraw import *
import hashlib


class TestTemplateDraw(unittest.TestCase):

    def test_validate_template_pixel_placement(self):
        template_body = [[30,10,97,49], [10,30,87,56], [10,30,127,59], [30,10,97,88], [10,80,107,98], [10,10,97,108], [10,10,117,108], [10,30,86,118], [10,30,127, 118], [10,10,97,178], [10,10,117,178], [10,30,87,188], [10,30,127,188], [30,28,97,59]]
        template_ghost_body = [[80, 10, 69, 35], [10, 20, 59, 45],[10, 20, 149, 45],[10, 80, 49, 65],[10, 80, 159, 65],[10, 10, 59, 145], [10, 10, 69, 135],[10, 10, 79, 145], [10, 10, 89, 135], [10, 10, 99, 145], [10, 10, 109, 135], [10, 10, 119, 145], [10, 10, 129, 135], [10, 10, 139, 145], [10, 10, 149, 135], [10, 10, 159, 145], [10, 20, 88, 70], [10, 20, 118, 70]]
        template1 = generate_template("Person", "Hello World")
        template2 = generate_template("Ghost", "Python")
        template3 = generate_template("", "3XA3")
        template4 = generate_template("Ghost", "Programming")
        for i in range(0, len(template1[0])):
            for j in range(0, len(template1[0][0])):
                self.assertEqual(template1[0][i][j], template_body[i][j])
                self.assertEqual(template3[0][i][j], template1[0][i][j])
        for i in range(0, len(template2[0])):
            for j in range(0, len(template2[0][0])):
                self.assertEqual(template2[0][i][j], template_ghost_body[i][j])
                self.assertEqual(template4[0][i][j], template2[0][i][j])
        for i in range(0, len(template2[0])):
            for j in range(0, len(template2[0][0])):
                self.assertNotEqual(template2[0][i][j] + 1, template_ghost_body[i][j])
                self.assertNotEqual(template4[0][i][j] + 1, template2[0][i][j])


if __name__ == '__main__':
    unittest.main()
