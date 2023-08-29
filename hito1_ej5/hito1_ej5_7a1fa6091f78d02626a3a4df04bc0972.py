#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el número de RUT a cadena
    rut = rut[::-1]  # Invertir la cadena de RUT
    serie = [2, 3, 4, 5, 6, 7]  # Serie numérica para multiplicar los dígitos del RUT
    suma = 0

    for i in range(len(rut)):
        suma += int(rut[i]) * serie[i % 6]

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

# Solicitar el número de RUT al usuario
rut = int(input("Ingrese el número de RUT: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      