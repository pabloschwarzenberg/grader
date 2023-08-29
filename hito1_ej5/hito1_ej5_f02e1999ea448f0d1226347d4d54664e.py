def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT para facilitar los cálculos
    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)


rut = input("Ingrese un número de RUT sin el dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
