#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

longitud = len(numero)
descomposicion = ""

if longitud >= 4:
    descomposicion += numero[-4] + "M + "
if longitud >= 3:
    descomposicion += numero[-3] + "C + "
if longitud >= 2:
    descomposicion += numero[-2] + "D + "
if longitud >= 1:
    descomposicion += numero[-1] + "U"

print(descomposicion)      