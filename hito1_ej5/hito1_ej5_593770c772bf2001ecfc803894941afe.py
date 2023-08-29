#Cálculo del dígito verificador de un rut
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
        digito_verificador = 0
    
    return digito_verificador

rut = int(input("Ingresa el número de RUT sin dígito verificador: "))
digito_verificador = calcular_digito_verificador(rut)
print("dv={digito_verificador}")
