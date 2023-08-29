def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]
    factor = 2
    suma = 0

    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    verificador = 11 - (suma % 11)
    if verificador == 11:
        dv = '0'
    elif verificador == 10:
        dv = 'K'
    else:
        dv = str(verificador)

    return dv


rut = input("Ingresa el número de RUT (sin dígito verificador): ")
dv = calcular_digito_verificador(rut)
print("dv=" + dv)
print("rut de forma chilena")
