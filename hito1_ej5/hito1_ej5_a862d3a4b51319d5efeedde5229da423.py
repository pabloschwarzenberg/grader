#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Revertir el RUT

    serie_numerica = [2, 3, 4, 5, 6, 7]
    suma_productos = 0

    indice_serie = 0
    for digito in rut_reverso:
        producto = int(digito) * serie_numerica[indice_serie]
        suma_productos += producto

        indice_serie += 1
        if indice_serie == len(serie_numerica):
            indice_serie = 0

    resto = suma_productos % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Pedir al usuario que ingrese el número de RUT
rut = int(input("Ingrese el número de RUT: "))

# Llamar a la función para calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv=" + str(digito_verificador))