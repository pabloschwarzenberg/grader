def calcular_dv(rut):
    multiplicador = 2
    suma = 0
    while rut > 0:
        digito = rut % 10
        rut //= 10
        suma += digito * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    dv = 11 - resto
    if dv == 11:
        return "0"
    elif dv == 10:
        return "K"
    else:
        return str(dv)

rut = int(input("Ingresa el RUT sin dígito verificador: "))
dv = calcular_dv(rut)
print("dv =", dv)