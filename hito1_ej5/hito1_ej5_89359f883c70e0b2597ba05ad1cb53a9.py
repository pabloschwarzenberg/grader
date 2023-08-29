def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena
    rut = rut[::-1]  # Invertir el RUT
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


# Solicitar el número de RUT al usuario
rut = int(input("Ingrese el número de RUT: "))

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Mostrar el resultado en pantalla
print("dv =", digito_verificador)
     