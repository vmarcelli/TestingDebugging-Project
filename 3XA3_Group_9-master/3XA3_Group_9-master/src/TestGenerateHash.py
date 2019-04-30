import unittest
import GenerateHash
import hashlib


class TestGenerateHash(unittest.TestCase):

    def test_retrieve_available_hash_encodings_returns_correct_list(self):
        self.assertEqual(GenerateHash.retrieve_available_hash_encodings(), hashlib.algorithms_available)
        self.assertNotEqual(GenerateHash.retrieve_available_hash_encodings, hashlib.algorithms_available.pop())

    def test_retrieve_hash_algorithm_returns_correct_hash(self):

        # either returns the correct algorithm, or the algorithm named isn't available
        # (must test this way since it's not known what algorithms will be available on any given machine)

        self.assertTrue(GenerateHash._retrieve_hash_algorithm('sha256').name == hashlib.sha256().name or
                        'sha256' not in hashlib.algorithms_available)
        self.assertTrue(GenerateHash._retrieve_hash_algorithm('md5').name == hashlib.md5().name or
                        'md5' not in hashlib.algorithms_available)
        self.assertTrue(GenerateHash._retrieve_hash_algorithm('bad_name').name == hashlib.md5().name or
                        'bad_name' not in hashlib.algorithms_available)

        self.assertTrue(isinstance(GenerateHash._retrieve_hash_algorithm('sha256'), type(hashlib.sha256())) or
                        'sha256' not in hashlib.algorithms_available)
        self.assertTrue(isinstance(GenerateHash._retrieve_hash_algorithm('md5'), type(hashlib.md5())) or
                        'md5' not in hashlib.algorithms_available)
        self.assertTrue(isinstance(GenerateHash._retrieve_hash_algorithm('bad_name'), type(hashlib.md5())) or
                        'bad_name' not in hashlib.algorithms_available)

        self.assertNotIn(GenerateHash._retrieve_hash_algorithm('test_name').name, "bad_name")
        # sending a non-existent algorithm name should return a random available algorithm
        self.assertTrue(GenerateHash._retrieve_hash_algorithm('test_name').name in hashlib.algorithms_available)

    def test_generate_hash_is_consistent(self):
        hash_val_1 = GenerateHash.generate_hash("test")
        hash_val_2 = GenerateHash.generate_hash("test")
        hash_val_3 = GenerateHash.generate_hash("other_test")
        self.assertEqual(hash_val_1, hash_val_2)
        self.assertNotEqual(hash_val_1, hash_val_3)


if __name__ == '__main__':
    unittest.main()
