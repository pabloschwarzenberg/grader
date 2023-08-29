def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1]
    factor = 2
    suma = 0

    for digito in rut_reversed:
        suma += int(digito) * factor
        factor = factor + 1 if factor < 7 else 2

    digito_verificador = 11 - (suma % 11)
    
    if digito_verificador == 10:
        return "k"
    elif digito_verificador == 11:
        return "0"
    else:
        return str(digito_verificador)

# Solicitar número de RUT al usuario
rut = int(input("Ingrese un número de RUT: "))

# Calcular dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir resultado
print("dv=" + digito_verificador)