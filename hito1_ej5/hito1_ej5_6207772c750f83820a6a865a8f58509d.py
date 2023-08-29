def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]  # Invertir el rut
    factors = [2, 3, 4, 5, 6, 7]  # Factores para multiplicar los dígitos del rut
    total = sum(int(digit) * factor for digit, factor in zip(reversed_rut, factors))
    digito_verificador = 11 - (total % 11)
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return 0
    else:
        return str(digito_verificador)

# Obtener el número de rut del usuario
rut = input("Ingrese un número de rut (sin el dígito verificador): ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv=" + dv)


# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv=" + dv)
