def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0

    return digito_verificador

# Solicitar al usuario que ingrese el rut
rut = input("Ingrese el número de RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)