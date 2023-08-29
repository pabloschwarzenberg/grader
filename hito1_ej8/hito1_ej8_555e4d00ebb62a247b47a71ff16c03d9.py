numero = input("Ingrese un número de hasta 4 dígitos: ")

# Validar que el número tenga hasta 4 dígitos
if len(numero) > 4:
    print("El número debe tener hasta 4 dígitos.")
    exit()

# Obtener cada dígito del número
unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) == 4 else 0

# Imprimir la descomposición del número
descomposicion = []
if miles > 0:
    descomposicion.append(str(miles) + "M")
if centenas > 0:
    descomposicion.append(str(centenas) + "C")
if decenas > 0:
    descomposicion.append(str(decenas) + "D")
if unidades > 0:
    descomposicion.append(str(unidades) + "U")

print(" + ".join(descomposicion))
