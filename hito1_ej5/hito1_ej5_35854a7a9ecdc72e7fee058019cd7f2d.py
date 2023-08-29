def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0

    return digito_verificador

# Solicitar al usuario el número de RUT
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)