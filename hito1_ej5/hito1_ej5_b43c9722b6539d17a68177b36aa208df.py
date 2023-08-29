#Cálculo del dígito verificador de un rut
from itertools import cycle

rut = input("Ingrese su rut: ")

reversed_digits = map(int, reversed(rut))
factors = cycle(range(2, 8))
s=sum(d * f for d, f in zip(reversed_digits, factors))
dv=(-s) % 11
if dv == 10:
  dv = "k"

print("dv="+str(dv))