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
    n =  key.shape[0]
    message += alphabet[-1]*(len(message) % n) # So that last block has enough elements
    code = ''
    for i in range(0, len(message), n):
        block = message[i:i+n]
        encodedBlock = HillEncodeBlock(alphabet, block, key)
        code += encodedBlock
    
    return code

def HillDecode(alphabet, message, key):
    m = len(alphabet)
    decodeKey = _matrixModInv(key, m)
    decoded = HillEncode(alphabet, message, decodeKey)

    return decoded
