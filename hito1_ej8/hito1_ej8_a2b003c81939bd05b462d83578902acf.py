#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Obtener la descomposición del número en unidades, decenas, centenas y miles
descomposicion = ""
longitud = len(numero)

if longitud == 4:
    descomposicion += numero[0] + "M + "

if longitud >= 3:
    descomposicion += numero[-3] + "C + "

if longitud >= 2:
    descomposicion += numero[-2] + "D + "

descomposicion += numero[-1] + "U"

# Imprimir el resultado
print("Descomposición:", descomposicion)    