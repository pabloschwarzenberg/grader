#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)
    
    factor = 2
    suma = 0
    
    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    resto = suma % 11
    digito_verificador = 11 - resto
    
    if digito_verificador == 10:
        return 'K'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

rut = input("Ingresa el número de RUT (sin dígito verificador): ")
dv = calcular_digito_verificador(rut)
print("dv =", dv)      