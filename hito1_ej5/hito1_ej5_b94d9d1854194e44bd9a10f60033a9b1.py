def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a una cadena de texto

    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador


# Solicitar el número de RUT al usuario
rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
