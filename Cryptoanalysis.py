import math
import Substitution

def Coprime(a, b):
    return math.gcd(a, b) == 1

def GetInvertibleResidues(n):
    residues = {x for x in range(1, n) if Coprime(x, n)}
    return residues

def AffineBruteforce(message, alphabet):
    n = len(alphabet)
    residues = GetInvertibleResidues(n)
    msg = message[:10]
    for a in residues:
        for b in range(n):
            text = Substitution.AffineDecode(alphabet, msg, a, b)
            print(a, b, text)

def AffineRecBruteforce(message, alphabet):
    n = len(alphabet)
    residues = GetInvertibleResidues(n)
    msg = message[:10]
    for a1 in residues:
        for a2 in residues:
            for b1 in range(n):
                for b2 in range(n):
                    text = Substitution.AffineRecDecode(alphabet, msg, a1, a2, b1, b2)
                    print(f'a1:{a1} a2:{a2} b1:{b1} b2:{b2} {text}')

print(AffineRecBruteforce('kqeurnzcyh', 'abcdefghijklmnopqrstuvwxyz'))
