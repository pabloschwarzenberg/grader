def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.zfill(8)  # Asegurar que el RUT tenga 8 dígitos rellenando con ceros a la izquierda si es necesario
    
    factor = 2
    suma = 0
    
    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor = (factor + 1) % 7 or 2
    
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K'
    else:
        return str(digito_verificador)

# Solicitar el RUT al usuario
rut = int(input("Ingrese un RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Mostrar el resultado
rut_completo = str(rut) + '-' + digito_verificador
print("El RUT completo con dígito verificador es:", rut_completo)

      