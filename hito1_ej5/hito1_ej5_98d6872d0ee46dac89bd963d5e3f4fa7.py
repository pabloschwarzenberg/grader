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
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Solicitar al usuario ingresar el número de RUT
rut = int(input("Ingrese el número de RUT: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
