#!/usr/bin/python

import sys

f = ???
msgs = [
    ???,
    ???,
    ???,
    ???,
    ???,
    ???,
    ???,
    ???,
]

def fraw_input(prompt):
    sys.stdout.write(prompt)
    return sys.stdin.readline()[:-1]

def s2n(d):
    return int(d.encode('hex'), 16)

def n2s(d):
    return str('%02x' % d).decode('hex')

def generateOTP(salt):
    e = 2**16 + 1
    N = 21290246318258757547497882016271517497806703963277216278233383215381949984056495911366573853021918316783107387995317230889569230873441936471
    return pow(s2n(salt), e, N)

def encrypt(msg, otp):
    notp = otp
    cipher = ''
    for l in msg:
        cipher += chr(ord(l) ^ (notp % 256))
        if notp == 0:
            notp = otp
        else:
            notp /= 256
    return cipher


otp1 = generateOTP(f)
print otp1
user_salt = fraw_input('SALT> ')
otp2 = generateOTP(user_salt)
otp  = otp1 ^ otp2
for m in msgs:
    print encrypt(m, otp).encode('hex')

uinput = fraw_input('PLAIN> ')
while uinput:
    print 'CIPHER> %s' % encrypt(uinput, otp).encode('hex')
    uinput = fraw_input('PLAIN> ')
