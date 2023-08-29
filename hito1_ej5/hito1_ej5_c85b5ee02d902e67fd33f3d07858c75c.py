#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_invertido = rut[::-1]  # Invertir el Rut
    multiplicador = 2
    suma = 0
    
    for digito in rut_invertido:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    resto = suma % 11
    digito_verificador = 11 - resto
    
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

# Pedir al usuario que ingrese un Rut sin dígito verificador
rut_input = input("Ingrese el Rut (sin dígito verificador): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut_input)

# Imprimir el resultado
print("dv=" + digito_verificador)

