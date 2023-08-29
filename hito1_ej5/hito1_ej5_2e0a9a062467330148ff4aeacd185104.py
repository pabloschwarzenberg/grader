#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  
    rut = rut[::-1]  
    multiplicador = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        dv = '0'
    elif digito_verificador == 10:
        dv = 'K'
    else:
        dv = str(digito_verificador)
    
    return dv



rut = int(input("Ingrese el número de Rut sin dígito verificador: "))


dv = calcular_digito_verificador(rut)


print("dv =", dv)
