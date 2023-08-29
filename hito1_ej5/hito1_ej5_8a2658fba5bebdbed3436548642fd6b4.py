def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]
    multiplicador = 2
    suma = 0
    
    for digito in rut_reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return 'dv=0'
    elif digito_verificador == 10:
        return 'dv=k'
    else:
        return 'dv=' + str(digito_verificador)

rut = input("Ingrese el RUT sin dígito verificador: ")
resultado = calcular_digito_verificador(rut)
print(resultado)
