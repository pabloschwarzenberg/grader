def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el rut para comenzar a multiplicar desde la posición más a la derecha
    multiplicador = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Solicitar al usuario ingresar el número de rut sin el dígito verificador
rut = int(input("Ingrese el número de Rut (sin el dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      