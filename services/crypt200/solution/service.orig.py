#!/usr/bin/python

# Unobfuscated Version

import base64
import math
import md5

hLen = 16
kLen = 256

def IntegerToString(i, l):
    return ("%%0%dx" % (2 * l)) % (i)

def Hash(data):
    return md5.new(data).digest()

def Checksum(k1, k2):
    cs1 = chr(sum([ord(i) for i in k1]) % 256)
    cs2 = chr(sum([ord(i) for i in k2]) % 256)
    cs3 = chr(reduce(lambda x,y: x*y, [ord(i) for i in k1], 1) % 256)
    cs4 = chr(reduce(lambda x,y: x*y, [ord(i) for i in k2], 1) % 256)
    return cs1 + cs2 + cs3 + cs4

def XOR(a, b):
    ax = [ord(i) for i in a]
    bx = [ord(i) for i in b]
    cx = [ax[i % len(ax)] ^ bx[i % len(bx)] for i in range(max(len(ax), len(bx)))]
    return ''.join([chr(i) for i in cx])

def PRF(k1, k2):
    h = Hash(k1 + ":" + k2)
    while len(h) < hLen:
        h += Hash(h)
    return h[:hLen]

def kdf1(pwd, additional=""):
    Z = pwd
    OtherInfo = additional
    d = int(math.ceil(1.0 * kLen / hLen))
    T = ""
    for Counter in range(d):
        C = IntegerToString(Counter, 4)
        T = T + Hash(Z + C + OtherInfo)
    return T[:kLen]

def kdf2(pwd, additional=""):
    Z = pwd
    OtherInfo = additional
    d = int(math.ceil(1.0 * kLen / hLen))
    T = ""
    for Counter in range(1, d+1):
        C = IntegerToString(Counter, 4)
        T = T + Hash(Z + C + OtherInfo)
    return T[:kLen]

def kdf3(pwd, additional="", pAmt=4):
    Z = pwd
    OtherInfo = additional
    d = int(math.ceil(1.0 * kLen / hLen))
    T = ""
    for Counter in range(d):
        C = IntegerToString(Counter, pAmt)
        T = T + Hash(C + Z + OtherInfo)
    return T[:kLen]

def pbkdf1(p, salt, c=16):
    if kLen > hLen:
        return "kLen is too long"
    T = Hash(p + salt)
    for i in range(2, c+1):
        T = Hash(T)
    return T[:kLen]

def pbkdf_schneier(p, salt, c=16):
    if kLen > hLen:
        return "kLen is too long"
    T = Hash(p + salt)
    for i in range(2, c+1):
        T = Hash(T + p + salt)
    return T[:kLen]

def pbkdf2(p, salt, c=16):
    d = int(math.ceil(1.0 * kLen / hLen))
    T = ""
    for i in range(1, d+1):
        F = U = PRF(p, salt + IntegerToString(i, 4))
        for j in range(2, c+1):
            U = PRF(p, U)
            F = XOR(F, U)
        T = T + F
    return T[:kLen]

kdfs = [
    kdf1,
    kdf2,
    kdf3,
    pbkdf1,
    pbkdf_schneier,
    pbkdf2
]

def generateOTP(u, p):
    salt = Checksum(u, p)
    c = u + ':' + p
    for kdf in kdfs:
        c = kdf(c, salt)
    return [ord(i) for i in c]


def encrypt(u, p, msg):
    otp = generateOTP(u, p)
    cipher = []
    for i in range(len(msg)):
        cipher.append(chr(ord(msg[i]) ^ otp[i % len(otp)]))
    return (u, base64.b64encode(''.join(cipher)))


def decrypt(u, p, cipherb64):
    cipher = base64.b64decode(cipherb64)
    otp = generateOTP(u, p)
    msg = []
    for i in range(len(cipher)):
        msg.append(chr(ord(cipher[i]) ^ otp[i % len(otp)]))
    return ''.join(msg)

# print encrypt(???, ???, ???)
# ('probe@mantle.earth', 'wPgJLjpNTkhOFPGFTsnVtAt7Z9Te4ZuBHHIR1kP8YtD+ilQESws=')
