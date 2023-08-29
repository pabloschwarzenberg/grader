#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    numero //= 10

    decenas = numero % 10
    numero //= 10

    centenas = numero % 10
    numero //= 10

    miles = numero

    return miles, centenas, decenas, unidades


# Solicitar número al usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número
miles, centenas, decenas, unidades = descomponer_numero(numero)

# Imprimir descomposición
print("Unidades:", unidades)
print("Decenas:", decenas)
print("Centenas:", centenas)
print("Miles:", miles)