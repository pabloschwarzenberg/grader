def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reverso = rut_str[::-1]
    factor = 2
    suma = 0

    for d in rut_reverso:
        suma += int(d) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

rut = input("Ingresa el Rut sin dígito verificador: ")
rut = int(rut)

dv = calcular_digito_verificador(rut)
print("dv =", dv)

