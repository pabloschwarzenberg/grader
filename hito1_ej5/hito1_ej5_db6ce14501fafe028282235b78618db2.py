#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT

    # Calcular dígito verificador
    factor = 2
    suma = 0
    for digito in rut:
        suma += int(digito) * factor
        factor = factor + 1 if factor < 7 else 2
    verificador = 11 - (suma % 11)
    if verificador == 11:
        return 0
    elif verificador == 10:
        return "K"
    else:
        return verificador


# Solicitar al usuario ingresar un número de RUT
rut = int(input("Ingrese un número de RUT: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv=" + str(digito_verificador))
      