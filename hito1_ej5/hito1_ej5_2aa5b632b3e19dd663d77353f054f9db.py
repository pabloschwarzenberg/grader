def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena de texto
    rut_reversed = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0
    for digito in rut_reversed:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "0"
    elif digito_verificador == 10:
        return "K"
    else:
        return str(digito_verificador)

# Solicitar al usuario ingresar el número de RUT
rut = int(input("Ingrese el número de RUT (sin dígito verificador): "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv=" + digito_verificador)
