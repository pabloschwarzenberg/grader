#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Invertir el Rut
    
    factor = 2
    suma = 0
    
    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 10:
        return "K"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

# Solicitar al usuario el número de Rut
rut = input("Ingrese el número de Rut: ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      