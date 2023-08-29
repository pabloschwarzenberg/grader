def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    # Calcula la suma de los productos de los dígitos por los multiplicadores
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    # Calcula el resto de la división por 11
    resto = suma % 11

    # Calcula el dígito verificador según las reglas
    if resto == 1:
        digito_verificador = 'K'
    elif resto == 0:
        digito_verificador = '0'
    else:
        digito_verificador = str(11 - resto)

    return digito_verificador

rut = int(input("Ingrese un número de RUT: "))
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
