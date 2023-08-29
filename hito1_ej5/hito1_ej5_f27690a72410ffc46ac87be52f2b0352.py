def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = 'K'

    return dv

numero_rut = input("Ingrese el número de RUT: ")
digito_verificador = calcular_digito_verificador(numero_rut)
print("dv =", digito_verificador)
