def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0
    for i in reversed(rut):
        suma += int(i) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

numero_rut = input("Ingresa el número de RUT (sin dígito verificador): ")
digito_verificador = calcular_digito_verificador(numero_rut)
print("dv =", digito_verificador)
