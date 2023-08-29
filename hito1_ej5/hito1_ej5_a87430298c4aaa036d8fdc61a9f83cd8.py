def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]
    multiplicador = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador

rut = input("Ingrese el número de rut (sin dígito verificador): ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
