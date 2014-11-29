#!/usr/bin/python

# Original Code with Plaintext

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

####

if __name__ == "__main__":
    ptexts = [
        "One small step for man, one giant leap for mankind."[::-1],
        "Goodnight stars, goodnight air, goodnight noises everywhere."[::-1],
        "The Light Side of the Moon: Reclaiming Your Lost Potential"[::-1],
        "Asiago, Blue, Cotja, Gruyere, Parmesan, Romano",
        "Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto",
        "Mary had a little lamb, His fleece was white as snow, And everywhere that Mary went, The lamb was sure to go.",
        "the quick brown fox jumps over the lazy dog",
        "Hey diddle diddle, The Cat and the fiddle, The Cow jumped over the moon.",
    ]
    
    flag = base64.b64encode('tesseract2014{OnlyUseFlagOnce}')
    key = [ord(i) for i in flag]
    
    ctexts = []
    
    for p in ptexts:
        pt = [ord(i) for i in p]
        #print pt
        c = encode(pt, key)
        #print c
        c = [(i % 256) for i in c]
        d = decode(c, key)
        #print d
        if d != pt:
            print "ERROR"
        ctexts.append(base64.b64encode(''.join([chr(i % 256) for i in c])))

    print ctexts
