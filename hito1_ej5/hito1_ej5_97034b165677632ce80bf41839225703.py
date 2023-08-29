#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for d in rut:
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 10:
        return "k"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

# Pedir al usuario que ingrese el RUT sin dígito verificador
rut_sin_dv = input("Ingresa el RUT sin dígito verificador: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut_sin_dv)

# Imprimir el resultado
print("dv =", digito_verificador)
dv = 0