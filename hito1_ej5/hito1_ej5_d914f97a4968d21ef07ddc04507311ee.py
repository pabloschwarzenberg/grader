def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1] 
    factor = 2
    suma = 0
    
    for digito in rut_reversed:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 10:
        return 'K'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

rut = int(input("Ingrese el RUT sin dígito verificador: "))
dv = calcular_digito_verificador(rut)
print("dv =", dv)
