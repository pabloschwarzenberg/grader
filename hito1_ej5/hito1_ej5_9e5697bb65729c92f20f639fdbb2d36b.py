#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_invertido = list(reversed([int(x) for x in str(rut)]))
    factores = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5]
    suma = sum(digito * factor for digito, factor in zip(rut_invertido, factores))
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador


# Obtener el RUT ingresado por el usuario
rut = input("Ingresa un número de RUT (sin puntos ni guión): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      