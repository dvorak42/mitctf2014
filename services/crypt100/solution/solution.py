#!/usr/bin/python
import base64

def checksum(p): return p[0] % 256

def encode(ptext, key):
    ctext = [0] * len(ptext)
    for i in range(len(ptext)):
        a = i
        b = (i+1) % len(ptext)
        ctext[a] = (ptext[a]^key[a % len(key)]) + (ptext[b]^key[a % len(key)])
    return ctext + [checksum(ptext)]

def decode(ctext, key):
    csum = ctext[-1]
    ctext = ctext[:-1]

    ptext = [0] * len(ctext)
    ptext[0] = csum
    for i in range(len(ptext) - 1):
        a = i
        b = (i+1) % len(ptext)
        ptext[b] = ((ctext[a] - (ptext[a]^key[a % len(key)])) ^ key[a % len(key)]) % 256
    return ptext

ctexts = [
    'Skx3JBWvcm2kXUlmqiVEMZCkGm8ODndla22PjLoPLk2iobVooplVl1uSdDEQoJt1c1FhLg==',
    'S1dXMR+QUydrU5lTZihaKEGOVFwPDiesa25KV/BgGwq1VJ4vbrdqsxZIp7BfgVslV5uonE8QVzJLTk6VLg==',
    'DVRhIhOdWz+CmneiI3CUF1w4gacRBya0dm1PGDeMmlhpvsqNtbFgZkZJr3kNsUSDpmJPsCVwhS1AQGw=',
    'PGJ2OBB78JRQXWZxznMwI15LbexnSReMYmdnSfCKQSNfsqYab3rwhEFSci8Z0EE=',
    'SFuysHHWVyVmR3NlzoY7M1t4X+xpNCOIYKTQbVIrFV/wir8FWaFVp17Se0QZjUcirPKJp2sPYxifzI5TGTYZm2ux0IhAGRkjPlM=',
    'LltTXU6taXaxrZC1XTxiMZmMLW4PUKySXVyrVnIJOhh4ZWcWYlOXnxlhVXlFlJtjYXFaY851LzKYlRNbFzMQn3FnZ1WYHiklqI3MG0tdl6oLXJywesBxda5xUq+cZ1Ykq6MIRxdVZJuvt0pFm00=',
    'HFGpZSiidCyrrGihXCGQdklXYKofGB2Lm69ZI1dsZBxxZW4tW5OldgtIU3Q=',
    'LWCleBGxZDJxqZitTRxSMY3MdDwRVZPKWaSdD3JWZBxxZXgvbaxssUnSeEARaYtQZJeSn1ghVTmYjx1bF2xknnG1kQR6BWxmSA==',
]

####
import string

ALL_POSSIBLE = [ord(i) for i in string.printable]
B64_POSSIBLE = [ord(i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/+=']
CMN_POSSIBLE = [ord(i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,. ']

def validOTPs(c, pa, otps):
    if not otps:
        otps = B64_POSSIBLE
    possible = []
    for pb in ALL_POSSIBLE:
        for k in otps:
            if c == ((pa^k) + (pb^k)) % 256:
                possible.append(k)
    return possible

def getOTP(c, p):
    otp = []
    ca = [ord(i) for i in base64.b64decode(c)]
    pa = [ord(i) for i in p]

    print ca[0]
    print (pa[0]^102)+(pa[1]^102)
    
    for i in range(len(pa) - 1):
        notp = []
        for k in B64_POSSIBLE:
            if ca[i] == (pa[i]^k) + (pa[(i+1) % len(pa)]^k):
                notp.append(k)
        otp.append(notp)
    print otp
    return otp

def crack(ctexts, otp=None):
    if not otp:
        otp = [None]

    new_otps = []
    for o in otp:
        next_otp = None
        for c in ctexts:
            if not o:
                next_otp = validOTPs(c[0], c[-1], next_otp)
                continue
            if len(c) <= len(o):
                continue
            ptext = decode(c, o)
            if len(ptext) <= len(o):
                continue
            next_otp = validOTPs(c[len(o)], ptext[len(o)], next_otp)

        if next_otp:
            for o2 in next_otp:
                if not o:
                    on = [o2]
                else:
                    on = o + [o2]
                v = 0
                u = 0
                for c in ctexts:
                    #print (on),
                    dec = decode(c, on)
                    if o and len(dec) < len(o) + 2:
                        continue
                    u += 1
                    if o:
                        #print ''.join([chr(i) for i in dec])[:len(o) + 2]
                        if dec[len(o) + 1] in CMN_POSSIBLE:
                            v += 1
                    else:
                        #print ''.join([chr(i) for i in dec])[:2]
                        if dec[1] in CMN_POSSIBLE:
                            v += 1
                #print v
                if v < 7:
                    continue
                #d = raw_input('> ')
                #if len(d) > 0 and d.lower()[0] == 'y':
                new_otps.append(on)
    print len(new_otps)
    if len(new_otps) > 0:
        return crack(ctexts, new_otps)
    return otp

#partials = [
#    getOTP(ctexts[4], 'Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn'),
#    getOTP(ctexts[6], 'the quick brown fox jumps over the lazy'),
#]

#iox = []
#mlen = min([len(x) for x in partials])
#for i in range(mlen):
#    i1 = partials[0][i]
#    for i2 in partials:
#        i1 = [x for x in i2[i] if x in i1]
#    iox.append(i1)
#print iox

initial = None
#initial = [iox]
#initial = [[100, 71, 86, 122, 99, 50, 86, 121, 89, 87, 78, 48, 77, 106, 65, 120, 78, 72]]

cr = crack([[ord(i) for i in base64.b64decode(c)] for c in ctexts], otp=initial)
print cr
for c in cr:
    for o in range(4):
        try:
            asx = ''.join([chr(i) for i in c])
            if o != 0:
                asx = asx[:-o]
            print base64.b64decode(asx)
            break
        except:
            pass

for o in range(4):
    try:
        asx = ''.join([chr(i) for i in cr[0]])
        if o != 0:
            asx = asx[:-o]
        key= base64.b64decode(asx)
    except:
        pass

####

for c in ctexts:
    ca = [ord(i) for i in base64.b64decode(c)]
    pa = decode(ca, [ord(i) for i in base64.b64encode(key)])
    print ''.join([chr(i) for i in pa])

