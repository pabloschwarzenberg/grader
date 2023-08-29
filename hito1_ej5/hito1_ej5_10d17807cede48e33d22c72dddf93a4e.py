from itertools import cycle

rut = input("Ingrese su rut sin dv: ")
reversed_digits = map(int, reversed(str(rut)))
factors = cycle(range(2, 8))
s = sum(d * f for d, f in zip(reversed_digits, factors))
dvNormal = -s % 11

if dvNormal == 10:
#    print("1--->",dvNormal)
    dvNormal = 'K'
    print('dv=',dvNormal)
elif dvNormal == 11:
#    print("2--->",dvNormal)
    dvNormal = 0
    print('dv= ',dvNormal)
else:
#    print("3--->",dvNormal)
    print('dv= ',dvNormal)