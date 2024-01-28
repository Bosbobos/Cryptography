import Substitution

msg = '''Please choose the operation:
0: exit
1: Simple substitution encode
2: Simple substitution decode
3: Affine encode
4: Affine decode
5: Recurrent Affine encode
6: Recurrent Affine decode
'''

if __name__ == '__main__':
    alphabet = input('Please enter the alphabet: ')
    func = int(input(msg))
    while(func != 0):
        match func:
            case 1:
                msg, key = input('Message, key: ').split(', ')
                print(Substitution.Simple(alphabet, msg, key))
            case 2:
                msg, key = input('Message, key: ').split(', ')
                print(Substitution.SimpleDecode(alphabet, msg, key))
            case 3:
                msg, *keys = input('Message, keyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.Affine(alphabet, msg, keyA, keyB))
            case 4:
                msg, *keys = input('Message, keyA, keyB: ').split(', ')
                keyA, keyB = map(int, keys)
                print(Substitution.AffineDecode(alphabet, msg, keyA, keyB))
            case 5:
                msg, *keys = input('Message, keyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRec(alphabet, msg, keyA1, keyA2, keyB1, keyB2))
            case 6:
                msg, *keys = input('Message, keyA1, keyA2, keyB1, keyB2: ').split(', ')
                keyA1, keyA2, keyB1, keyB2 = map(int, keys)
                print(Substitution.AffineRecDecode(alphabet, msg, keyA1, keyA2, keyB1, keyB2))
        
        func = int(input('Operation: '))
