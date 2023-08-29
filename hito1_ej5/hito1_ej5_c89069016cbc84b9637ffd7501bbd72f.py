#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Revertir el orden del RUT
    factor = 2
    suma = 0

    for digito in rut_reverso:
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

# Solicitar al usuario ingresar el RUT sin dígito verificador
rut_sin_dv = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut_sin_dv)

# Imprimir el resultado
print("dv =", dv)
