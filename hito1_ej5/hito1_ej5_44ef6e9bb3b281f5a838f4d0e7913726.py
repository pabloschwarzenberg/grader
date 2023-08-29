#Cálculo del dígito verificador de un rut
from itertools import cycle

dni = input('Ingresa el rut sin digito verificador: ')

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = (-s) % 11
    return 'k' if dv == 10 else dv

print('dv={}'.format( digito_verificador( dni ) ))