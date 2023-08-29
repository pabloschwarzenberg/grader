def descomponer_numero(numero):
    # Descomposición en unidades, decenas, centenas y miles
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

    # Construcción de la representación en texto
    representacion = ""
    if miles > 0:
        representacion += f"{miles}M "
    if centenas > 0:
        representacion += f"{centenas}C "
    if decenas > 0:
        representacion += f"{decenas}D "
    if unidades > 0:
        representacion += f"{unidades}U"

    # Impresión de la descomposición
    print(representacion)


# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número y mostrar la descomposición
descomponer_numero(numero)




