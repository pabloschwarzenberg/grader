def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reverso = rut_str[::-1]
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    digito_verificador = 11 - resto if resto != 0 else 0

    if digito_verificador == 10:
        digito_verificador = 'k'

    return digito_verificador

rut = input("Ingrese el número de RUT sin el dígito verificador: ")

digito_verificador = calcular_digito_verificador(rut)

print("dv=" + str(digito_verificador))
