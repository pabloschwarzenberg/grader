# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Obtener la longitud del número ingresado
longitud = len(numero)

# Completar con ceros a la izquierda si es necesario
if longitud < 4:
    numero = numero.zfill(4)

# Descomponer el número en unidades, decenas, centenas y miles
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
if unidades > 0:
    descomposicion += str(unidades) + "U"

print(descomposicion)
      