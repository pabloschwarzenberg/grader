#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT
    
    factor = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    resto = suma % 11
    dv = 11 - resto
    
    if dv == 10:
        return "k"
    elif dv == 11:
        return "0"
    else:
        return str(dv)

# Obtener el RUT del usuario
rut = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
