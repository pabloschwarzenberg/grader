def descomponer_numero(numero):
    # Convertir el número a cadena y rellenar con ceros a la izquierda si es necesario
    numero_str = str(numero).zfill(4)

    # Obtener los dígitos individuales
    unidades = int(numero_str[-1])
    decenas = int(numero_str[-2])
    centenas = int(numero_str[-3])
    miles = int(numero_str[-4])

    # Crear la representación de cada dígito
    unidades_repr = "{}U".format(unidades) if unidades != 0 else ""
    decenas_repr = "{}D".format(decenas) if decenas != 0 else ""
    centenas_repr = "{}C".format(centenas) if centenas != 0 else ""
    miles_repr = "{}M".format(miles) if miles != 0 else ""

    # Combinar las representaciones en una cadena
    descomposicion = " + ".join(filter(None, [miles_repr, centenas_repr, decenas_repr, unidades_repr]))

    return descomposicion

# Pedir al usuario que ingrese un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener la descomposición del número
descomposicion = descomponer_numero(numero)

# Imprimir el resultado
print(descomposicion)