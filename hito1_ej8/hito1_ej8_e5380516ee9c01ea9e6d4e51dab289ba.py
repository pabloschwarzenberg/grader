def descomponer_numero(numero):
    # Descomponer el número en unidades, decenas, centenas y miles
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    # Crear una lista con las partes descompuestas del número
    descomposicion = []
    if miles > 0:
        descomposicion.append(str(miles) + "M")
    if centenas > 0:
        descomposicion.append(str(centenas) + "C")
    if decenas > 0:
        descomposicion.append(str(decenas) + "D")
    if unidades > 0:
        descomposicion.append(str(unidades) + "U")

    # Devolver la descomposición como una cadena de texto
    return " + ".join(descomposicion)


numero = int(input("Ingrese un número de hasta 4 dígitos: "))

descomposicion = descomponer_numero(numero)
print("Descomposición:", descomposicion)
