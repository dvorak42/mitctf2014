data = open('service.log').read().strip().split('---')

code = data[0].strip().split('\n')
trace = data[1].strip().split('\n')

real_code = [x for x in code]
translation = {}

for l in trace[:-1]:
    line = int(l[1:].split(':')[0].strip())
    val = l[1:].split(':')[1].strip()
    if val != '???':
        real_code[line] = val
        translation[code[line]] = val
    
print real_code
print translation

for i in range(len(real_code)):
    if real_code[i] in translation.keys():
        real_code[i] = translation[real_code[i]]

for i in real_code:
    print i

