numero = input("Ingrese un número de hasta 4 dígitos: ")
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Rellenar con ceros a la izquierda si es necesario
    numero = numero.zfill(4)

    unidades = int(numero[-1])
    decenas = int(numero[-2])
    centenas = int(numero[-3])
    miles = int(numero[-4])

    descomposicion = ""
    if miles >= 0:
        descomposicion += str(miles) + 'M+'
    if centenas >= 0:
        descomposicion += str(centenas) + "C+"
    if decenas >= 0:
        descomposicion += str(decenas) + "D+"
    if unidades >= 0:
        descomposicion += str(unidades) + "U"

    print(descomposicion)


