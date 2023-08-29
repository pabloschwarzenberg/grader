def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        return "0"
    elif digito_verificador == 10:
        return "K"
    else:
        return str(digito_verificador)

# Solicitar el número de RUT al usuario
rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
