def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    # Calcula la suma ponderada de los dígitos del RUT en sentido inverso
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    # Calcula el dígito verificador
    dv = 11 - (suma % 11)
    if dv == 11:
        dv = '0'
    elif dv == 10:
        dv = 'K'
    else:
        dv = str(dv)

    return dv

# Ejemplo de uso
rut = input("Ingresa el RUT sin dígito verificador: ")
dv = calcular_digito_verificador(rut)
print("dv=" + dv)
