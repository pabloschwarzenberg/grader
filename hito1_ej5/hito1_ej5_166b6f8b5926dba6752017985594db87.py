#Cálculo del dígito verificador de un rut
from itertools import cycle
def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11!=10:
        return (-s) % 11
    else:
        return 'k'
rutIngreso=int(input("Ingrese su rut sin digito verificador:\n"))
print("dv=",digito_verificador(rutIngreso))