#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1]  # Invertir el RUT
    factor = 2
    suma = 0
    
    # Calcular la suma ponderada de los dígitos del RUT invertido
    for d in rut_reversed:
        suma += int(d) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    # Calcular el dígito verificador
    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador


# Solicitar al usuario el número de RUT sin dígito verificador
rut_input = input("Ingrese el número de RUT sin dígito verificador: ")
rut = int(rut_input)

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", digito_verificador)
      