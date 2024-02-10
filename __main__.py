import Substitution

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


msg = '''Please choose the operation:
0: exit
1: Simple substitution encode
2: Simple substitution decode
3: Affine encode
4: Affine decode
5: Recurrent Affine encode
6: Recurrent Affine decode
7: Change alphabet
'''

if __name__ == '__main__':
    alphabet = input('Please enter the alphabet: ')
    message = input('Please enter the message: ')
    val = Validate(message, alphabet)
    func = int(input(msg))
    while(func != 0):
        match func:
            case 1:
                key = input('Key: ')
                print(Substitution.Simple(alphabet, val, key))
            case 2:
                key = input('Key: ')
                print(Substitution.SimpleDecode(alphabet, val, key))
            case 3:
                keys = input('KeyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.Affine(alphabet, val, keyA, keyB))
            case 4:
                keys = input('KeyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.AffineDecode(alphabet, val, keyA, keyB))
            case 5:
                keys = input('KeyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRec(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 6:
                keys = input('KeyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRecDecode(alphabet, val, keyA1, keyA2, keyB1, keyB2))
            case 7:
                alphabet = input('Please enter the alphabet: ')

        message = input('Please enter the message: ')
        val = Validate(message, alphabet)
        func = int(input('Operation: '))
