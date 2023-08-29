def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el rut

    factor = 2
    suma = 0

    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2

    resto = suma % 11
    dv = 11 - resto

    if dv == 11:
        return 0
    elif dv == 10:
        return "K"
    else:
        return dv


# Programa principal
rut = int(input("Ingrese el rut (sin dígito verificador): "))
dv = calcular_digito_verificador(rut)
print("dv =", dv)

