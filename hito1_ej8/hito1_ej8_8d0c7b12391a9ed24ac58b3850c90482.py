#Descomponer un número


def descomponer_numero(numero):
    miles = numero // 1000
    numero = numero % 1000
    centenas = numero // 100
    numero = numero % 100
    decenas = numero // 10
    unidades = numero % 10

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0 or descomposicion == "":
        descomposicion += str(unidades) + "U"

    return descomposicion

# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))
 
descomposicion = descomponer_numero(numero)

# Imprimir el resultado
print(descomposicion)