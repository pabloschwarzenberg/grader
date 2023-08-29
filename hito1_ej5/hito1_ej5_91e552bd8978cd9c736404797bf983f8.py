def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena de caracteres
    rut = rut.zfill(8)  # Asegurarse de que el RUT tenga 8 dígitos (rellenar con ceros a la izquierda si es necesario)

    # Calcular el dígito verificador
    factor = 2
    suma = 0
    for i in range(7, -1, -1):
        suma += int(rut[i]) * factor
        factor += 1
        if factor == 8:
            factor = 2
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

# Solicitar el RUT al usuario
rut = input("Ingrese el RUT (sin puntos ni guión): ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv=" + str(dv))
