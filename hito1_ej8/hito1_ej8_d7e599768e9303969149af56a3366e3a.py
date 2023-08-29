def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades >= 0:
        descomposicion += str(unidades) + "U"
    else:
        descomposicion += "0U"

    return descomposicion


numero = int(input("Ingresa un número de hasta 4 dígitos: "))

descomposicion = descomponer_numero(numero)

print("La descomposición del número es:", descomposicion)
