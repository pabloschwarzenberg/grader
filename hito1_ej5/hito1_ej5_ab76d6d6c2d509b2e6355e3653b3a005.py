def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]
    multiplicador = 2
    suma = 0

    for d in rut:
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador
    
rut_input = input("Ingresa el RUT sin dígito verificador: ")
try:
    rut = int(rut_input)
    digito_verificador = calcular_digito_verificador(rut)
    print("dv =", digito_verificador)
except ValueError:
    print("Error: Ingresa un número válido como RUT.")