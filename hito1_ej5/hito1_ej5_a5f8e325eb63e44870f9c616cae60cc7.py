#Cálculo del dígito verificador de un rut
RUT = int(input("ingrese rut:"))
from itertools import cycle
def digito_verificador(RUT):
    reversed_digits = map(int, reversed(str(RUT)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
if digito_verificador(RUT) == 10:
    print("dv=k")
if digito_verificador(RUT)!=10:
    print("dv="+ str(digito_verificador(RUT)))
    