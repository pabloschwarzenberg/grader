def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Revertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar el RUT al usuario
rut = int(input("Ingrese el RUT sin dígito verificador: "))

# Calcular el dígito verificador y mostrar el resultado
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)