#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]
    factor = 2
    suma = 0
    
    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)


rut = input("Ingresa un RUT sin dígito verificador: ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)
      