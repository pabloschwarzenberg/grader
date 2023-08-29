numero = input("Ingresa un numero de hasta 4 digitos: ")

if len(numero) > 4:
    print("El numero que ingresaste tiene mas de 4 digitos.")
else:
    while len(numero) < 4:
        numero = "0" + numero

    unidades = int(numero[-1])
    decenas = int(numero[-2])
    centenas = int(numero[-3])
    miles = int(numero[-4])

    descomposicion = ""

    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    print(descomposicion)