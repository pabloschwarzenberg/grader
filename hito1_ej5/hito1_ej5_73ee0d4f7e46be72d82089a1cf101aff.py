#Cálculo del dígito verificador de un rut
from itertools import cycle
rut = eval(input("ingrese el rut sin guion"))

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

if digito_verificador(rut)==10:
        print("dv=k")
else:
    print("dv=",digito_verificador(rut))     