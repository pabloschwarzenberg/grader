#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Pedir al usuario que ingrese un número de RUT sin el dígito verificador
rut = int(input("Ingrese un número de RUT (sin dígito verificador): "))

# Calcular el dígito verificador y imprimirlo
dv = calcular_digito_verificador(rut)
print("dv =", dv)
