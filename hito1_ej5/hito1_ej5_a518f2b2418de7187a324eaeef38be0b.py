#Cálculo del dígito verificador de un rut
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
   
x = input("rut")

dv = digito_verificador(x)

if dv == 10:
    dv = "K"
print("dv=",dv)      