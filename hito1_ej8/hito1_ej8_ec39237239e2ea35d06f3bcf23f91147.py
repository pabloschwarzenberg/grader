n = input('Ingrese un numero:')

n= n.zfill(4)

u = int(n[3])
d = int(n[2])
c = int(n[1])
m = int(n[0])

r = ''

if m >= 0:
    r+= str(m) +'M +'
if c >= 0:
    r+= str(c) +'C +'
if d >= 0:
    r+= str(d) +'D +'
if u >= 0 or r == '':
    r+= str(u) +'U'

print(r)