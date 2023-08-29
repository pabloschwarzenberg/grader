def calcular_digito_verificador(rut):
    rut = rut.replace(".", "").replace("-", "")
    rut_reverso = rut[::-1]
    multiplicador = 2
    suma = 0

    for d in rut_reverso:
        suma += int(d) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

rut = input("Ingrese el RUT sin dígito verificador: ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)
