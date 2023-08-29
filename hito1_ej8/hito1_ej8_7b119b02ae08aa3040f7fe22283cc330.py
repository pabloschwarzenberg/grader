#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Obtener el número de dígitos ingresado
num_digitos = len(numero)

# Agregar ceros a la izquierda si el número tiene menos de 4 dígitos
numero = numero.zfill(4)

# Descomponer el número en unidades, decenas, centenas y miles
unidades = int(numero[-1])
decenas = int(numero[-2])
centenas = int(numero[-3])
miles = int(numero[-4])

# Crear una lista con las partes descompuestas
descomposicion = []
if miles > 0:
    descomposicion.append(f"{miles}M")
if centenas > 0:
    descomposicion.append(f"{centenas}C")
if decenas > 0:
    descomposicion.append(f"{decenas}D")
if unidades > 0:
    descomposicion.append(f"{unidades}U")

# Imprimir la descomposición del número
print(" + ".join(descomposicion))
