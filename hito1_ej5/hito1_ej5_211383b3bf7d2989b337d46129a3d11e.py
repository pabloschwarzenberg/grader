def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Revertir el RUT
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador


rut = int(input("Ingresa el RUT sin el dígito verificador: "))
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
