def calcular_digito_verificador(rut):
    rut_reverso = str(rut)[::-1]  # Revertir el RUT
    factor = 2
    suma = 0
    
    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    
    return digito_verificador

rut = input("Ingrese un número de RUT (sin dígito verificador): ")
dv = calcular_digito_verificador(rut)

print("dv =", dv)

      