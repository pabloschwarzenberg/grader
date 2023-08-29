#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_digits = map(int, reversed(rut))

    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv = (-s) % 11

    return str(dv).upper() if dv < 10 else 'K'

rut = input("Ingresa el número de RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)      