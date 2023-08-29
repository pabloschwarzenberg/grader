def calcular_digito_verificador(rut):
    rut_str = str(rut)
    reversed_rut = rut_str[::-1]  # Invertir el Rut
    factor = 2
    suma = 0
    
    for digito in reversed_rut:
        suma += int(digito) * factor
        factor += 1
        if factor == 8:
            factor = 2
    
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Solicitar al usuario ingresar el Rut sin el dígito verificador
rut_sin_dv = int(input("Ingrese el Rut sin dígito verificador: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut_sin_dv)

# Imprimir el resultado
print("dv =", dv)
