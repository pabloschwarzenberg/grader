rut1 = []
rut1.append(str(input('Ingrese el tur: ')))
rut = rut1[0]
sum = 0
r = len(rut)
v = 2
i = 0
u = r - 1
t = r
while i < r:
    dig = int(rut[u:t]) * v
    i += 1
    v += 1
    u = u - 1
    t = t - 1
    if v == 8:
        v = 2
    sum = sum + dig
print('La suma total es: ', sum)
mod = (sum // 11)
res = sum - (11 * mod)
ver = 11 - res
if ver < 10:
    print('dv=%d' %(ver))
if ver == 11:
    ver = 0
    print('dv=%d' %(ver))
if ver == 10:
    ver = 'K'
    print('dv=%s' %(ver))