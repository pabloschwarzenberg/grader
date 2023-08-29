#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]  # Invertir el Rut
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

# Solicitar al usuario un número de Rut
numero_rut = input("Ingrese un número de Rut (sin dígito verificador): ")

# Calcular dígito verificador
digito_verificador = calcular_digito_verificador(numero_rut)

# Imprimir el resultado
print("dv =", digito_verificador)