import unittest
import Substitution

class SubstitutionTest(unittest.TestCase):

    def test_VigenereEncode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "TEST"
        key = "TEST"

        result = Substitution.VigenereEncode(alphabet, message, key)
        self.assertEqual(result, "MIKM")

    def test_RepeatKeyVigenereEncode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "TESTINGCASEREPEATKEY"
        key = "TEST"

        result = Substitution.RepeatKeyVigenereEncode(alphabet, message, key)
        self.assertEqual(result, "MIKMBRYVTWWKXTWTMOWR")

    def test_RepeatKeyVigenereDecode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "TESTINGCASEREPEATKEY"
        key = "TEST"

        result = Substitution.RepeatKeyVigenereEncode(alphabet, message, key)
        decoded = Substitution.RepeatKeyVigenereDecode(alphabet, result, key)
        self.assertEqual(decoded, message)

    def test_KeyByTextVigenereEncode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "K"

        result = Substitution.KeyByTextVigenereEncode(alphabet, message, key)
        self.assertEqual(result, "MTPNIHUXRPWF")

    def test_KeyByTextVigenereDecode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "KA"

        result = Substitution.KeyByTextVigenereEncode(alphabet, message, key)
        decoded = Substitution.KeyByTextVigenereDecode(alphabet, result, key)
        self.assertEqual(decoded, message)

    def test_KeyByCipertextVigenereEncode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "K"

        result = Substitution.KeyByCipertextVigenereEncode(alphabet, message, key)
        self.assertEqual(result, "MDBQJXDUUJQO")

    def test_KeyByCipertextVigenereDecode(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message = "CRYPTOGRAPHY"
        key = "KA"

        result = Substitution.KeyByCipertextVigenereEncode(alphabet, message, key)
        decoded = Substitution.KeyByCipertextVigenereDecode(alphabet, result, key)
        self.assertEqual(decoded, message)

if __name__ == '__main__':
    unittest.main()
