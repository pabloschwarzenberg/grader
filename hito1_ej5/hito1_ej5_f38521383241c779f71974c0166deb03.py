#Cálculo del dígito verificador de un rut
from itertools import cycle
r = int(input("Ingrese rut:"))
def dv (r) :
    reversed_digits = map (int, reversed(str(r)))
    factors = cycle(range(2, 8))
    s = sum(d*f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
if dv (r) == 10:
    print("dv=k")
if dv (r) != 10:
    print("dv=" + str(dv(r)))