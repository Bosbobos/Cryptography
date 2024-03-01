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

def VigenereEncode(alphabet, message, key):
    m = len(alphabet)

    code = ''
    for i in range(len(message)):
        x = alphabet.index(message[i])
        k = alphabet.index(key[i])
        y = (x + k) % m
        code += alphabet[y]

    return code

def _invertKey(alphabet, key):
    m = len(alphabet)

    inverted = ''
    for i in range(len(key)):
        k = alphabet.index(key[i])
        inverted += alphabet[(-k)%m]

    return inverted

def RepeatKeyVigenereEncode(alphabet, message, key):
    n = int(len(message) / len(key)) + (len(message) % len(key) > 0) # ceil without importing math
    repeated = key * n
    newKey = repeated[:len(message)]

    return VigenereEncode(alphabet, message, newKey)

def RepeatKeyVigenereDecode(alphabet, message, key):
    invertedKey = _invertKey(alphabet, key)
    
    return RepeatKeyVigenereEncode(alphabet, message, invertedKey)

def KeyByTextVigenereEncode(alphabet, message, key):
    delta = len(message) - len(key)
    newKey = key + message[:delta]

    return VigenereEncode(alphabet, message, newKey)

def KeyByTextVigenereDecode(alphabet, message, key):
    m = len(alphabet)

    code = ''
    for i in range(len(message)):
        kLetter = key[i] if len(key) > i else code[i - len(key)]
        k = alphabet.index(kLetter)
        x = alphabet.index(message[i])
        y = (x - k) % m
        code += alphabet[y]

    return code

def KeyByCipertextVigenereEncode(alphabet, message, key):
    m = len(alphabet)

    code = ''
    for i in range(len(message)):
        kLetter = key[i] if len(key) > i else code[i-len(key)]
        k = alphabet.index(kLetter)
        x = alphabet.index(message[i])
        y = (x + k) % m
        code += alphabet[y]

    return code

def KeyByCipertextVigenereDecode(alphabet, message, key):
    delta = len(message) - len(key)
    newKey = key + message[:delta]
    invertedKey = _invertKey(alphabet, newKey)

    return VigenereEncode(alphabet, message, invertedKey)
