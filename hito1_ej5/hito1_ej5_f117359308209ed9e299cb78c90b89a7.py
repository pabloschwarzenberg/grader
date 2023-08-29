def calcular_digito_verificador(rut):
    # Convertir el RUT en una cadena y revertirlo
    rut_str = str(rut)[::-1]

    # Lista con los factores del algoritmo
    factores = [2, 3, 4, 5, 6, 7]

    # Inicializar el valor acumulado
    acumulado = 0

    # Calcular el dígito verificador
    for i in range(len(rut_str)):
        acumulado += int(rut_str[i]) * factores[i % 6]

    # Calcular el dígito verificador como el complemento a 11 del acumulado
    digito_verificador = 11 - (acumulado % 11)

    # Manejar casos especiales para el dígito verificador
    if digito_verificador == 11:
        return "0"
    elif digito_verificador == 10:
        return "K"
    else:
        return str(digito_verificador)


# Obtener el RUT desde el usuario
rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Calcular y mostrar el dígito verificador
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + digito_verificador)
