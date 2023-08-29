rut = int(input("Indique su rut sin el dígito verificador: "))

var1 = rut // 10000000
var2 = (rut - var1 * 10000000) // 1000000
nark = (rut - var1 * 10000000 - var2 * 1000000) // 100000
are = (rut - var1 * 10000000 - var2 * 1000000 - nark * 100000) // 10000
tpose = (rut - var1 * 10000000 - var2 * 1000000 - nark * 100000 - are * 10000) // 1000
pknm = (rut - var1 * 10000000 - var2 * 1000000 - nark * 100000 - are * 10000 - tpose * 1000) // 100
nou = (rut - var1 * 10000000 - var2 * 1000000 - nark * 100000 - are * 10000 - tpose * 1000 - pknm * 100) // 10
top = (rut % 10)

fx = 3 * var1
ax = 2 * var2
sx = 7 * nark
nk = 6 * are
gx = 5 * tpose
ox = 4 * pknm
xx = 3 * nou
xy = 2 * top

suma = fx + ax + sx + nk + gx + ox + xx + xy

sas = suma % 11

zzz = 11 - sas

if zzz == 10:
    print("dv=k")
elif zzz == 11:
    print("dv=0")
else:
    print("dv={}".format(zzz))
