def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a una cadena de texto
    rut = rut[::-1]  # Invertir el RUT
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)

# Pedir al usuario que ingrese un número de RUT
rut = input("Ingrese un número de RUT: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)