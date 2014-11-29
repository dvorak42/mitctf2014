#!/usr/bin/python

import struct
import sys

def toarray(f):
    return [[ord(e) for e in r] for r in f.split('\n')]

def compress(frames, speed):
    bframe = toarray(frames[0])
    
    width = len(bframe[0])
    height = len(bframe)
    
    data = 'XMNG'
    data += struct.pack('<H', width)
    data += struct.pack('<H', height)
    data += struct.pack('<f', speed)
    data += struct.pack('<I', len(frames))
    lframe = [[0 for c in range(width)] for r in range(height)]
    for i in range(len(frames)):
        nframe = toarray(frames[i])
        if width != len(nframe[0]) or height != len(nframe):
            print i
            print len(nframe[0]), len(nframe)
        for r in range(height):
            for c in range(width):
                data += struct.pack('<B', (nframe[r][c] - lframe[r][c]) % 256)
        lframe = nframe

    return data


if len(sys.argv) < 2:
    sys.exit()

data = [s.strip() for s in open(sys.argv[1]).read().split('\n====\n')]

speed = float(data[0])
frames = data[1:]

data = compress(frames, speed)

f = open("%s.xmng" % (sys.argv[1]), "w")
f.write(data)
f.close()
