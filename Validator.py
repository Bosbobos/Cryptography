import numpy as np

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


def ValidateMatrix(alphabet, matrix):
    m = len(alphabet)
    det = int(np.round(np.linalg.det(matrix)))
    gcd = np.gcd(m, det)
    return gcd == 1

def ValidateMatrixesDimensions(matrix1, matrix2):
    return matrix1.shape == matrix2.shape
