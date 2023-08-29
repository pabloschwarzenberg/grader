def calcular_digito_verificador(rut):
    rut = rut[::-1]  # Invertimos el orden de los dígitos del RUT
    multiplicador = 2
    suma = 0
    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = '0'
    return str(digito_verificador)

rut = input("Ingrese el RUT (sin puntos ni guion): ")
digito_verificador = calcular_digito_verificador(rut)
print("Dv = ", digito_verificador)