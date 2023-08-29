#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Invertir el RUT
    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0

    return digito_verificador

# Obtener el RUT del usuario
rut = input("Ingrese un número de RUT: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el dígito verificador
print("dv =", dv)      