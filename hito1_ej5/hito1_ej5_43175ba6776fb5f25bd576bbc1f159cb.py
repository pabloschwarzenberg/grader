def calcular_digito_verificador(rut):
    # Convertir el RUT a una lista de dígitos
    rut_digitos = [int(digito) for digito in str(rut)]

    # Coeficientes para calcular el dígito verificador
    coeficientes = [2, 3, 4, 5, 6, 7]

    # Calcular la suma ponderada de los dígitos
    suma_ponderada = sum([digito * coeficiente for digito, coeficiente in zip(reversed(rut_digitos), coeficientes)])

    # Calcular el dígito verificador
    digito_verificador = 11 - (suma_ponderada % 11)

    # Manejar casos especiales para dígitos verificadores mayores a 9
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)


if __name__ == "__main__":
    # Solicitar al usuario ingresar el RUT
    rut = input("Ingrese el RUT (sin dígito verificador): ")

    # Llamar a la función para calcular el dígito verificador
    digito_verificador = calcular_digito_verificador(rut)

    # Imprimir el resultado
    print("dv =", digito_verificador)