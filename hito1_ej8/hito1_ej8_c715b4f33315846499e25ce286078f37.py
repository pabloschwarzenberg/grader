numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar que el número ingresado tenga hasta 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
    exit()

# Descomponer el número en unidades, decenas, centenas y miles
unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) == 4 else 0

# Imprimir la descomposición
descomposicion = ""

if miles > 0:
    descomposicion += f"{miles}M "

if centenas > 0:
    descomposicion += f"{centenas}C "

if decenas > 0:
    descomposicion += f"{decenas}D "

if unidades > 0:
    descomposicion += f"{unidades}U "

print(f"Descomposición: {descomposicion}")
