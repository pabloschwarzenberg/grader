def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reverso = rut_str[::-1]  # Invertir el orden del RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return "dv=K"
    elif digito_verificador == 11:
        return "dv=0"
    else:
        return "dv=" + str(digito_verificador)

rut = int(input("Ingrese el número de RUT sin el dígito verificador: "))

digito_verificador = calcular_digito_verificador(rut)
print(digito_verificador)