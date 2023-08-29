#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Obtener las unidades, decenas, centenas y miles del número
if len(numero) == 1:
    unidades = int(numero[0])
    decenas = 0
    centenas = 0
    miles = 0
elif len(numero) == 2:
    unidades = int(numero[1])
    decenas = int(numero[0])
    centenas = 0
    miles = 0
elif len(numero) == 3:
    unidades = int(numero[2])
    decenas = int(numero[1])
    centenas = int(numero[0])
    miles = 0
else:
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

# Imprimir la descomposición
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
descomposicion += str(unidades) + "U"

print("Descomposición:", descomposicion)
