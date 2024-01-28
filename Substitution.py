def Simple(alphabet, message, key):
    if len(alphabet) != len(key):
        raise Exception('Key should be the same length as the alphabet')
    substitution = {alphabet[i]: key[i] for i in range(len(key))}
    code = ''.join(substitution[x] for x in message)

    return code


def SimpleDecode(alphabet, message, key):
    return Simple(key, message, alphabet)


def Affine(alphabet, message, keyA, keyB):
    m = len(alphabet)

    code = ''
    for i in range(len(message)):
        x = alphabet.index(message[i])
        y = (x*keyA + keyB) % m
        code += alphabet[y]

    return code


def AffineDecode(alphabet, message, keyA, keyB):
    m = len(alphabet)
    invertedA = pow(keyA, -1, m)
    invertedB = -keyB*invertedA

    return Affine(alphabet, message, invertedA, invertedB)


def AffineRec(alphabet, message, keyA1, keyA2, keyB1, keyB2):
    m = len(alphabet)

    keyA = [keyA1, keyA2]
    keyB = [keyB1, keyB2]
    for i in range(2, len(message)):
        keyA += [keyA[i-1]*keyA[i-2]]
        keyB += [keyB[i-1]+keyB[i-2]]

    code = ''
    for i in range(len(message)):
        x = alphabet.index(message[i])
        y = (x*keyA[i] + keyB[i]) % m
        code += alphabet[y]

    return code

def AffineRecDecode(alphabet, message, keyA1, keyA2, keyB1, keyB2):
    m = len(alphabet)

    keyA = [keyA1, keyA2]
    keyB = [keyB1, keyB2]
    for i in range(2, len(message)):
        keyA += [keyA[i-1]*keyA[i-2]]
        keyB += [keyB[i-1]+keyB[i-2]]

    code = ''
    for i in range(len(message)):
        y = alphabet.index(message[i])
        x = ((y - keyB[i]) * pow(keyA[i],-1, m)) % m
        code += alphabet[x]

    return code

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = 'CRYPTOGRAPHY'

keySimple = 'PASWORDBCEFGHIJKMNQLUVTXYZ'
encoded = Simple(alphabet, msg, keySimple)
decoded = SimpleDecode(alphabet, encoded, keySimple)
print(encoded, decoded)

keyA = 3
keyB = 10
encodedAf = Affine(alphabet, msg, keyA, keyB)
decodedAf = AffineDecode(alphabet, encodedAf, keyA, keyB)
print(encodedAf, decodedAf)

keyA2 = 5
keyB2 = 4
encodedAfRec = AffineRec(alphabet, msg, keyA, keyA2, keyB, keyB2)
decodedAfRec = AffineRecDecode(alphabet, encodedAfRec, keyA, keyA2, keyB, keyB2)
print(encodedAfRec, decodedAfRec)
