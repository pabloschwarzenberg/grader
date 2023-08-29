def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]
    factor = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    resto = suma % 11
    digito_verificador = 11 - resto
    
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

rut = int(input("Ingrese el número de Rut sin dígito verificador: "))

digito_verificador = calcular_digito_verificador(rut)

print("dv =", digito_verificador)
