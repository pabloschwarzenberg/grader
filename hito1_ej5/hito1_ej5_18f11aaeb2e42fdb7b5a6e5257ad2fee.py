def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1]  # Revertir el Rut
    factor = 2
    suma = 0

    for digito in rut_reversed:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar al usuario el Rut
rut = int(input("Ingrese un número de Rut: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
