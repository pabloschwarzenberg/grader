def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    digito_verificador = 11 - resto if resto != 0 else 0
    if digito_verificador == 10:
        digito_verificador = "k"

    return digito_verificador

rut = input("Ingrese el RUT sin el dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + str(digito_verificador))
