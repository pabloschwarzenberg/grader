#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]  # Invertir el RUT
    factor = 2
    suma = 0

    for d in reversed_rut:
        suma += int(d) * factor
        factor = factor + 1 if factor < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar al usuario el RUT sin dígito verificador
rut = int(input("Ingresa el RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      