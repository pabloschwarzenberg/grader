def descomponer_numero(numero):
    miles = numero // 1000
    numero %= 1000
    centenas = numero // 100
    numero %= 100
    decenas = numero // 10
    unidades = numero % 10

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

# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número en unidades, decenas, centenas y miles
descomposicion = descomponer_numero(numero)

# Imprimir la descomposición
print("Descomposición:", descomposicion)
