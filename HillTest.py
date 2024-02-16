import unittest
import numpy as np
import Hill

class TestHillEncode(unittest.TestCase):

    def test_HillEncode(self):
        # Test case 1
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "HELLO"
        key = np.array([[6, 24], [13, 16]])
        expected_output = "IZSHIK"
        self.assertEqual(Hill.HillEncode(alphabet, message, key), expected_output)

        # Test case 2
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "WORLD"
        key = np.array([[6, 24], [13, 16]])
        expected_output = "AQCHUX"
        self.assertEqual(Hill.HillEncode(alphabet, message, key), expected_output)

    def test_HillDecode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "HELLO"
        key = np.array([[1, 4], [3, 7]])
        encoded = Hill.HillEncode(alphabet, message, key)
        decoded = Hill.HillDecode(alphabet, encoded, key)
        self.assertEqual(decoded[:5], message)

if __name__ == "__main__":
    unittest.main()
