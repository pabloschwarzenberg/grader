#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el Rut a una cadena de caracteres
    rut_reverso = rut[::-1]  # Invertir el orden de los caracteres del Rut
    factor = 2
    suma = 0
    
    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    
    return digito_verificador

# Pedir al usuario que ingrese el Rut sin dígito verificador
rut = int(input("Ingrese el Rut sin dígito verificador: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)     