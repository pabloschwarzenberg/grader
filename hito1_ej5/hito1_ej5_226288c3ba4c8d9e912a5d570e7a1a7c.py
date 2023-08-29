def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]  # Invertimos el RUT para facilitar el cálculo
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Pedimos al usuario que ingrese el número de RUT
rut = int(input("Ingrese un número de RUT: "))

# Calculamos el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimimos el resultado
print("dv=" + str(dv))
