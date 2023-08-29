def descomponer_numero(numero):
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    miles = numero
    return miles, centenas, decenas, unidades

# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

miles, centenas, decenas, unidades = descomponer_numero(numero)

# Imprimir la descomposición del número
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M "
if centenas > 0:
    descomposicion += str(centenas) + "C "
if decenas > 0:
    descomposicion += str(decenas) + "D "
if unidades > 0:
    descomposicion += str(unidades) + "U "

print("Descomposición:", descomposicion)