#Descomponer un número
def descomponer_numero(numero):
    miles = numero // 1000
    centenas = int(numero / 100) % 10
    decenas = (numero // 10) % 10
    unidades = numero % 10

    descomposicion = "{}M + {}C + {}D + {}U".format(miles, centenas, decenas, unidades)
    return descomposicion

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número
descomposicion = descomponer_numero(numero)

# Imprimir el resultado
print(descomposicion)

# Imprimir el resultado
print(descomposicion)