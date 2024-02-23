import numpy as np
import Substitution
import Hill, Validator

def CreateKeyMatrix(alphabet):
    n = int(input('Number of key\'s rows: '))
    print('Please, separate elements of each row with a space.')
    inputStrings = []
    for i in range(n):
        row = input(f'{i+1} row: ')
        inputStrings.append(row)
    arr = list([int(x) for x in row.split()] for row in inputStrings)
    key = np.array(arr)
    if not Validator.ValidateMatrix(alphabet, key):
        raise Exception('Key matrix\'s determinant should be coprime with the alphabet\'s power.')

    return key


def EnterAlphabet():
    english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet = ''
    msg = input('Write 1 for english alphabet, 2 for russian, or write your own alphabet: ')
    match msg:
        case '1': alphabet = english
        case '2': alphabet = russian
        case _: alphabet = msg

    return alphabet

msg = '''Please choose the operation:
0: exit
1: Change alphabet
2: Simple substitution encode
3: Simple substitution decode
4: Affine encode
5: Affine decode
6: Recurrent Affine encode
7: Recurrent Affine decode
8: Hill encode
9: Hill decode
10: Recurrent Hill encode
11: Recurrent Hill decode
'''


if __name__ == '__main__':
    alphabet = EnterAlphabet()
    message = input('Please enter the message: ')
    val = Validator.Validate(message, alphabet)
    func = int(input(msg))
    while(func != 0):
        match func:
            case 1:
                alphabet = EnterAlphabet()
            case 2:
                key = input('Key: ')
                print(Substitution.Simple(alphabet, val, key))
            case 3:
                key = input('Key: ')
                print(Substitution.SimpleDecode(alphabet, val, key))
            case 4:
                keys = input('KeyA keyB: ').split()
                keyA, keyB = map(int, keys)
                print(Substitution.Affine(alphabet, val, keyA, keyB))
            case 5:
                keys = input('KeyA keyB: ').split()
                keyA, keyB = map(int, keys)
                print(Substitution.AffineDecode(alphabet, val, keyA, keyB))
            case 6:
                keys = input('KeyA1 keyA2 keyB1 keyB2: ').split()
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRec(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 7:
                keys = input('KeyA1 keyA2 keyB1 keyB2: ').split()
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRecDecode(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 8:
                key = CreateKeyMatrix(alphabet)
                print(Hill.HillEncode(alphabet, val, key))
            case 9:
                key = CreateKeyMatrix(alphabet)
                print(Hill.HillDecode(alphabet, val, key))
            case 10:
                key1 = CreateKeyMatrix(alphabet)
                key2 = CreateKeyMatrix(alphabet)
                if not Validator.ValidateMatrixesDimensions(key1, key2):
                    raise Exception('Key\'s dimensions should be the same')
                print(Hill.RecHillEncode(alphabet, val, key1, key2))
            case 11:
                key1 = CreateKeyMatrix(alphabet)
                key2 = CreateKeyMatrix(alphabet)
                if not Validator.ValidateMatrixesDimensions(key1, key2):
                    raise Exception('Key\'s dimensions should be the same')                
                print(Hill.RecHillDecode(alphabet, val, key1, key2))

        message = input('Please enter the message: ')
        val = Validator.Validate(message, alphabet)
        func = int(input('Operation: '))
