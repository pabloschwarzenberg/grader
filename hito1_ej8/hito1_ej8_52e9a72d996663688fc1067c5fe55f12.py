def descomponer_numero(numero):
    miles = numero // 1000
    centenas = (numero // 100) % 10
    decenas = (numero // 10) % 10
    unidades = numero % 10

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M"
        descomposicion += "+"
    if centenas >= 0:
        descomposicion += str(centenas) + "C"
        descomposicion += "+"
    if decenas >= 0:
        descomposicion += str(decenas) + "D"
        descomposicion += "+"
    if unidades >= 0:
        descomposicion += str(unidades) + "U"

    return descomposicion


# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número en unidades, decenas, centenas y miles
descomposicion = descomponer_numero(numero)

# Imprimir la descomposición
print("Para", numero, "debe imprimir:", descomposicion)
