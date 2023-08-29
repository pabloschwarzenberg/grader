# Descomponer un número
# Obtener el número del usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener los dígitos del número
unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

# Imprimir la descomposición
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M+"
if centenas > 0:
    descomposicion += str(centenas) + "C+"
if decenas > 0:
    descomposicion += str(decenas) + "D+"
descomposicion += str(unidades) + "U"

# Eliminar el último "+" si existe
if descomposicion.endswith("+"):
    descomposicion = descomposicion[:-1]

print("Descomposición:", descomposicion)
