def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    # Calcular la suma ponderada de los dígitos del RUT
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # Calcular el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return "0"
    elif digito_verificador == 10:
        return "K"
    else:
        return str(digito_verificador)

# Solicitar al usuario el RUT
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
