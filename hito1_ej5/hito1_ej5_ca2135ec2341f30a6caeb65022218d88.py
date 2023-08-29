def calcular_digito_verificador(rut):
    rut_str = str(rut)
    multiplicador = 2
    suma = 0

    # Calcular la suma ponderada de los dígitos del RUT en sentido inverso
    for i in range(len(rut_str) - 1, -1, -1):
        suma += int(rut_str[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    # Calcular el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Solicitar el número de RUT al usuario
rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      