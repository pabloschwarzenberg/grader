#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena de texto
    rut = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    verificador = 11 - (suma % 11)
    if verificador == 11:
        return 'dv=0'
    elif verificador == 10:
        return 'dv=K'
    else:
        return 'dv=' + str(verificador)


# Ejemplo de uso
rut = input("Ingrese el RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print(digito_verificador)