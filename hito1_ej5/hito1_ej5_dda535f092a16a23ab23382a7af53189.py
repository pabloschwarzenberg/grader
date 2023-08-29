def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)
    factor = 2
    suma = 0
    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor = (factor + 1) % 8 or 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        dv = 0
    elif digito_verificador == 10:
        dv = 'K'
    else:
        dv = digito_verificador
    return dv
rut = input("Ingrese el RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=",digito_verificador)