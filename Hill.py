import numpy as np

def _matrixModInv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    detInv = pow(det, -1, modulus)

    inverted = (detInv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus

    return inverted

def HillEncodeBlock(alphabet, message, key):
    encodedMsg = np.array([alphabet.index(x) for x in message])
    msgMatrix = encodedMsg.reshape(len(encodedMsg), 1)
    codeMatrix = np.dot(key, msgMatrix)
    code = ''.join([alphabet[int(x % len(alphabet))] for x in codeMatrix.flatten()])
    return code

def HillEncode(alphabet, message, key):
    blockLen = key.shape[0]
    message += alphabet[-1]*(len(message) % blockLen) # So that last block has enough elements
    code = ''
    for i in range(0, len(message), blockLen):
        block = message[i:i+blockLen]
        encodedBlock = HillEncodeBlock(alphabet, block, key)
        code += encodedBlock
    
    return code

def HillDecode(alphabet, message, key):
    m = len(alphabet)
    decodeKey = _matrixModInv(key, m)
    decoded = HillEncode(alphabet, message, decodeKey)

    return decoded

def RecHillEncode(alphabet, message, key1, key2):
    blockLen = key1.shape[0]
    message += alphabet[-1]*(len(message) % blockLen) # So that last block has enough elements
    blocksNum = len(message) // blockLen
    keys = [key1, key2]
    for i in range(2, blocksNum):
        keyN = np.matmul(keys[i-2], keys[i-1]) % len(alphabet)
        keys.append(keyN)
    
    code = ''
    for i in range(blocksNum):
        block = message[i*blockLen:(i+1)*blockLen]
        encodedBlock = HillEncodeBlock(alphabet, block, keys[i])
        code += encodedBlock
    
    return code

def RecHillDecode(alphabet, message, key1, key2):
    m = len(alphabet)
    blockLen = key1.shape[0]
    message += alphabet[-1]*(len(message) % blockLen) # So that last block has enough elements
    blocksNum = len(message) // blockLen
    keys = [_matrixModInv(key1, m), _matrixModInv(key2, m)]
    for i in range(2, blocksNum):
        keyN = np.matmul(keys[i-1], keys[i-2]) % m
        keys.append(keyN)
    
    code = ''
    for i in range(blocksNum):
        block = message[i*blockLen:(i+1)*blockLen]
        encodedBlock = HillEncodeBlock(alphabet, block, keys[i])
        code += encodedBlock
    
    return code
