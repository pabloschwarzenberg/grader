def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1]
    multiplicador = 2
    suma = 0
    
    for digito in rut_reversed:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"
    
    return digito_verificador

# Solicitar al usuario el RUT
rut = int(input("Ingrese el RUT (sin dígito verificador): "))

# Calcular el dígito verificador utilizando la función calcular_digito_verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el dígito verificador
print("dv =", digito_verificador)
      