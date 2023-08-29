def calcular_digito_verificador(rut):
    rut = str(rut)
    reverse_rut = rut[::-1]
    factor = 2
    suma = 0

    for digito in reverse_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)


rut = input("Ingrese el RUT (sin dígito verificador): ")


digito_verificador = calcular_digito_verificador(rut)


print("dv =", digito_verificador)