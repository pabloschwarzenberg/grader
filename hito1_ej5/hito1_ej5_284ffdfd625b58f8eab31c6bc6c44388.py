def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_digits = map(int, reversed(rut))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return str((11 - s % 11) % 11)

rut = input("Ingrese un RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)