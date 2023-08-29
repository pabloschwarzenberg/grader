# Solicitar al usuario un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Validar que el número sea válido
if not numero.isdigit() or len(numero) > 4:
    print("El número ingresado no es válido.")
    exit()

# Obtener los dígitos individuales del número
unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) >= 4 else 0

# Imprimir la descomposición en unidades, decenas, centenas y miles
descomposicion = ""

if miles > 0:
    descomposicion += str(miles) + "M + "

if centenas > 0:
    descomposicion += str(centenas) + "C + "

if decenas > 0:
    descomposicion += str(decenas) + "D + "

if unidades > 0 or (miles == 0 and centenas == 0 and decenas == 0):
    descomposicion += str(unidades) + "U"

print("Descomposición:", descomposicion)