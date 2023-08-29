from itertools import cycle

rut= input()

reversed_digits = map(int, reversed(str(rut)))
factors = cycle(range(2, 8))
s = sum(d * f for d, f in zip(reversed_digits, factors))
dv=((-s) % 11)
if dv == 10:
    dv = 'K'
    
elif dv == 11:
    dv = 0
print('dv=',dv)



    
