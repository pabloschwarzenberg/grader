#Descomponer un número
numero = input("Ingresa un número de hasta 4 dígitos: ")

# Obtener la longitud del número ingresado
longitud = len(numero)

# Completar el número con ceros a la izquierda si es necesario
numero = numero.zfill(4)

# Obtener los dígitos individuales del número
miles = int(numero[0])
centenas = int(numero[1])
decenas = int(numero[2])
unidades = int(numero[3])

# Construir la descomposición en unidades, decenas, centenas y miles
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M "
if centenas > 0:
    descomposicion += str(centenas) + "C "
if decenas > 0:
    descomposicion += str(decenas) + "D "
if unidades > 0:
    descomposicion += str(unidades) + "U"

print("Descomposición:", descomposicion)
