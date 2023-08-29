def descomponer_numero(numero):
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    miles = numero % 10

    descomposicion = ""

    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    return descomposicion

numero = int(input("Ingrese un número de hasta 4 dígitos: "))

descomposicion = descomponer_numero(numero)
print("Descomposición:", descomposicion)
