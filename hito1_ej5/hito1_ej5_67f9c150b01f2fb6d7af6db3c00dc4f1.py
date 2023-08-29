#Cálculo del dígito verificador de un rut      
rut = int(input("Ingrese su RUT:"))
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

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

dv = calcular_digito_verificador(rut)

print("dv =", dv)