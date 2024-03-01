import unittest
import Substitution

class TestVigenereFunctions(unittest.TestCase):

    def test_Vigenere(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "TEST"
        key = "TEST"

        result = Substitution.Vigenere(alphabet, message, key)
        self.assertEqual(result, "MIKM")

    def test_RepeatKeyVigenere(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "TESTINGCASEREPEATKEY"
        key = "TEST"

        result = Substitution.RepeatKeyVigenere(alphabet, message, key)
        self.assertEqual(result, "MIKMBRYVTWWKXTWTMOWR")

    def test_KeyByTextVigenere(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "K"

        result = Substitution.KeyByTextVigenere(alphabet, message, key)
        self.assertEqual(result, "MTPNIHUXRPWF")

    def test_KeyByCipertextVigenere(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "K"

        result = Substitution.KeyByCipertextVigenere(alphabet, message, key)
        self.assertEqual(result, "MDBQJXDUUJQO")

if __name__ == '__main__':
    unittest.main()
