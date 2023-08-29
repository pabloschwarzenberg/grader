def calcularDigitoVerificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el rut
    factor = 2
    suma = 0
    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    return digito_verificador

rut = int(input("Ingresa el rut: "))
dv = calcularDigitoVerificador(rut)
print("dv =", dv)
