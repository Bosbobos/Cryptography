import numpy as np
import Substitution
import Hill

def Validate(message, alphabet):
    if alphabet == alphabet.lower():
        msg = message.lower()
    elif alphabet == alphabet.upper():
        msg = message.upper()
    else:
        msg = message
    extra = [x for x in set(msg) if x not in alphabet]
    for x in extra:
        msg = msg.replace(x, '')

    return msg


def CreateKeyMatrix():
    n = int(input('Number of key\'s rows: '))
    print('Please, separate elements of each row with a ", ".')
    inputStrings = []
    for i in range(n):
        row = input(f'{i+1} row: ')
        inputStrings.append(row)

    key = np.array([list(map(int, row.split(', ')) for row in inputStrings)])
    return key

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
'''

if __name__ == '__main__':
    alphabet = input('Please enter the alphabet: ')
    message = input('Please enter the message: ')
    val = Validate(message, alphabet)
    func = int(input(msg))
    while(func != 0):
        match func:
            case 1:
                alphabet = input('Please enter the alphabet: ')
            case 2:
                key = input('Key: ')
                print(Substitution.Simple(alphabet, val, key))
            case 3:
                key = input('Key: ')
                print(Substitution.SimpleDecode(alphabet, val, key))
            case 4:
                keys = input('KeyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.Affine(alphabet, val, keyA, keyB))
            case 5:
                keys = input('KeyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.AffineDecode(alphabet, val, keyA, keyB))
            case 6:
                keys = input('KeyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRec(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 7:
                keys = input('KeyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRecDecode(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 8:
                key = CreateKeyMatrix()
                print(Hill.HillEncode(alphabet, val, key))
                

        message = input('Please enter the message: ')
        val = Validate(message, alphabet)
        func = int(input('Operation: '))
