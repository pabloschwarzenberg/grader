#Cálculo del dígito verificador de un rut
from itertools import cycle
a = input()

reversed_digits = map(int, reversed(str(a)))
factors = cycle(range(2, 8))
s = sum(d * f for d, f in zip(reversed_digits, factors))
b = (-s) % 11
if b >= 10:
    print("dv=k")
else:
    print("dv=", (-s) % 11)
   