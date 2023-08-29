#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]  # Invertir el RUT
    factor = 2
    suma = 0
    
    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    
    return digito_verificador

# Solicitar al usuario que ingrese el número de RUT
rut = int(input("Ingrese el número de RUT: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
      