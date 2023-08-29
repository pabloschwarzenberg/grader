def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "dv=0"
    elif digito_verificador == 10:
        return "dv=K"
    else:
        return "dv=" + str(digito_verificador)

numero_rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))
resultado = calcular_digito_verificador(numero_rut)
print(resultado)
