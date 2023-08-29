def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]
    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

# Solicitar RUT al usuario
rut = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir resultado
print("dv =", digito_verificador)
