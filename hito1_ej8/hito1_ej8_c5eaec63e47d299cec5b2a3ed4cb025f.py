numero = input("Ingresa un número de hasta 4 dígitos: ")

# Validar que el número sea de hasta 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
    exit()

# Añadir ceros a la izquierda si el número tiene menos de 4 dígitos
numero = numero.zfill(4)

# Obtener los dígitos individuales
unidades = int(numero[3])
decenas = int(numero[2])
centenas = int(numero[1])
miles = int(numero[0])

# Crear una lista de términos con sus respectivos dígitos
terminos = []
if miles > 0:
    terminos.append(f"{miles}M")
if centenas > 0:
    terminos.append(f"{centenas}C")
if decenas > 0:
    terminos.append(f"{decenas}D")
if unidades > 0:
    terminos.append(f"{unidades}U")

# Imprimir la descomposición
print(" + ".join(terminos))

     