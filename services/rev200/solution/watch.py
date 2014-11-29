#!/usr/bin/python

import os
import struct
import sys
import time

data = ""

def pull(f):
    global data
    result = struct.unpack_from(f, data)
    data = data[struct.calcsize(f):]
    return result[0]

def fromarray(a):
    
    return '\n'.join([''.join([chr(i) for i in r]) for r in a])

def decompress(d):
    global data
    data = d
    
    assert pull('<I') == struct.unpack('<I', 'XMNG')[0]
    width = pull('<H')
    height = pull('<H')
    speed = pull('<f')
    nframes = pull('<I')

    frames = []
    lframe = [[0 for c in range(width)] for r in range(height)]
    for i in range(nframes):
        nframe = [[0 for c in range(width)] for r in range(height)]
        for r in range(height):
            for c in range(width):
                nframe[r][c] = (lframe[r][c] + pull('<B')) % 256
        frames.append(fromarray(nframe))
        lframe = nframe

    return (frames, speed)


if len(sys.argv) < 2:
    sys.exit()

(frames, speed) = decompress(open(sys.argv[1]).read())

for frame in frames:
    os.system('clear')
    print frame
    time.sleep(60.0 / speed)
