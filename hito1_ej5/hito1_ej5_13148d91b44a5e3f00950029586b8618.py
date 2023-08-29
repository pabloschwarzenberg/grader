def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reverso = rut_str[::-1]
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar el número de RUT al usuario
rut = input("Ingrese el número de RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv =", digito_verificador)




      