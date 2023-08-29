#Cálculo del dígito verificador de un rut
from itertools import cycle

def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_digits = map(int, reversed(rut))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = (11 - s % 11)
    if dv == 10:
        return 'k'
    elif dv == 11:
        return '0'
    else:
        return str(dv)

# Solicitar el número de rut al usuario
rut = input("Ingresa el número de rut (sin puntos ni guiones): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv=" + digito_verificador)
