#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Descomposición en unidades, decenas, centenas y miles
unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) == 4 else 0

# Impresión de la descomposición
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
if unidades > 0:
    descomposicion += str(unidades) + "U"

# Eliminar el último signo "+" si existe
if descomposicion.endswith(" + "):
    descomposicion = descomposicion[:-3]

print("Descomposición:", descomposicion)