#!/usr/bin/python 

def magic():
    with open('flag') as f:
        return f.read().strip() + 0

evil = [
    'CRASH',
    '__',
    'exec',
    'eval',
    'input',
    'import',
    'evil',
    'file',
    'magic',
]

def handle():
    print '>',
    data = raw_input('').strip()
    if len(data) > 32:
        return False

    for k in evil:
        data = data.replace(k, 'CRASH')
    if len(data) > 32:
        return False
    data = data.replace('CRASH', '')
    exec data

    return True

if __name__ == '__main__':
    print "Venus Probe v0.3"
    print "Location: Orbit around Venus"
    print "Mission: Locate ???"

    running = True
    while running:
        try:
            running = handle()
        except:
            running = False
    print "Goodbye!"

