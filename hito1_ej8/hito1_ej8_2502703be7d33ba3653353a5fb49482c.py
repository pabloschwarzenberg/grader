def descomponer_numero(num):
    # Validar que el número no tiene más de 4 dígitos
    if num > 9999 or num < 0:
        return "Error: El número debe ser un entero positivo de hasta 4 dígitos."

    # Descomposición del número
    unidades = num % 10
    num = num // 10
    decenas = num % 10
    num = num // 10
    centenas = num % 10
    num = num // 10
    miles = num

    # Crear la representación del número descompuesto
    representacion = []
    if miles > 0:
        representacion.append("{}M".format(miles))
    if centenas > 0:
        representacion.append("{}C".format(centenas))
    if decenas > 0:
        representacion.append("{}D".format(decenas))
    if unidades > 0:
        representacion.append("{}U".format(unidades))

    return " + ".join(representacion)


# Pedir al usuario un número y descomponerlo
num = int(input("Introduce un número de hasta 4 dígitos: "))
print(descomponer_numero(num))
