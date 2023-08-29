#Cálculo del dígito verificador de un rut
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))

    return (-s) % 11

numero_rut = input("Ingresa un número de RUT sin dígito verificador: ")
digito_verif = digito_verificador(numero_rut)
print("DV = ", digito_verif)

if digito_verif == 10:
    print("DV = K")