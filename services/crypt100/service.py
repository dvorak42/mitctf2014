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

    for p0 in range(256):
        ptext = [0] * len(ctext)
        ptext[0] = p0
        for i in range(len(ptext)):
            a = i
            b = (i+1) % len(ptext)
            ptext[b] = ((ctext[a] - (ptext[a]^key[a % len(key)])) ^ key[a % len(key)]) % 256
        if checksum(ptext) == csum:
            return ptext
    return None

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

key = ???

for c in ctexts:
    ca = [ord(i) for i in base64.b64decode(c)]
    pa = decode(ca, [ord(i) for i in base64.b64encode(key)])
    print ''.join([chr(i) for i in pa])

