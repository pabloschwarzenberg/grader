def calcular_digito_verificador(rut):
    rut = str(rut)
    reversed_rut = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0
    
    for digito in reversed_rut:
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 10:
        return "k"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

# Solicitar RUT al usuario
rut = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)