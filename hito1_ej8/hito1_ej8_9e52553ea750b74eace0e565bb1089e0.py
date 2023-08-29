#Descomponer un número
def descomponer_numero(numero):
    digitos = [int(d) for d in str(numero)]

    descomposicion = ""

    if len(digitos) == 4:
        descomposicion += str(digitos[0]) + "M "
    if len(digitos) >= 3:
        descomposicion += str(digitos[-3]) + "C "
    if len(digitos) >= 2:
        descomposicion += str(digitos[-2]) + "D "
    if len(digitos) >= 1:
        descomposicion += str(digitos[-1]) + "U"

    return descomposicion

# Pedir al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número en unidades, decenas, centenas y miles
descomposicion = descomponer_numero(numero)

# Imprimir el resultado
print("Descomposición:", descomposicion)


