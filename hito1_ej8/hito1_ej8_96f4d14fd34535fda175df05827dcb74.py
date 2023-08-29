#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M+"
    if centenas > 0 or miles > 0:
        descomposicion += str(centenas) + "C+"
    if decenas > 0 or centenas > 0 or miles > 0:
        descomposicion += str(decenas) + "D+"
    descomposicion += str(unidades) + "U"

    return descomposicion

# Solicitar número al usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número en unidades, decenas, centenas y miles
descomposicion = descomponer_numero(numero)

# Imprimir el resultado
print(descomposicion)
