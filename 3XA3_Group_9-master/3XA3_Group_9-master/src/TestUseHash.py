import unittest
import UseHash


class TestUseHash(unittest.TestCase):
    def test_split_hash(self):
        self.assertEqual(UseHash._split_hash("0123456789abcdef", 4, 3), ["0123", "4567", "89ab"])
        self.assertEqual(UseHash._split_hash("0123456789abcdef", 4, 4), ["0123", "4567", "89ab", "cdef"])
        self.assertNotEqual(UseHash._split_hash("0123456789abcdef", 4, 4), ["012", "456", "89a", "cde"])
        self.assertRaises(IndexError, UseHash._split_hash, "0123456789abcdef", 4, 7)

    def test_hex_to_rgb(self):
        self.assertEqual(UseHash._hex_to_rgb("ffffff"), (255, 255, 255))
        self.assertEqual(UseHash._hex_to_rgb("abcabc"), (171, 202, 188))
        self.assertNotEqual(UseHash._hex_to_rgb("abcabc"), (0, 0, 0))


    def test_hash_to_colors(self):
        self.assertEqual(UseHash.hash_to_colours("0123456789abcdef0123456789abcdef0123456789abcdef"),
                         [(1, 35, 69), (103, 137, 171), (205, 239, 1), (35, 69, 103), (137, 171, 205),
                          (239, 1, 35), (69, 103, 137), (171, 205, 239)])

    def test_hash_to_value_in_range(self):
        self.assertIn(UseHash.hash_to_value_in_range("0123456789abcdef", 16), range(0, 16))
        self.assertIn(UseHash.hash_to_value_in_range("0123456789abcdef", 5), range(0, 5))
        self.assertIn(UseHash.hash_to_value_in_range("0123456789abcdef", 200), range(0, 200))
        self.assertNotIn(UseHash.hash_to_value_in_range("0123456789abcdef", 16), range(16, 50))
        self.assertRaises(IndexError, UseHash.hash_to_value_in_range, "0", 17)
        # testing to check that IndexError is not thrown in edge case
        self.assertIn(UseHash.hash_to_value_in_range("0", 16), range(0, 16))


if __name__ == '__main__':
    unittest.main()
