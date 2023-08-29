#Cálculo del dígito verificador de un rut
 def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el Rut a una cadena de caracteres
    rut = rut[::-1]  # Invertir el Rut para facilitar el cálculo

    factor = 2
    suma = 0

    for d in rut:
        suma += int(d) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador


# Pedir al usuario que ingrese un número de Rut
rut = int(input("Ingrese un número de Rut: "))

# Llamar a la función para calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)     