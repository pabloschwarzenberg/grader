#Descomponer un número
# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Asegurarse de que el número tenga hasta 4 dígitos
numero = numero.zfill(4)

# Obtener cada dígito del número
unidades = int(numero[3])
decenas = int(numero[2])
centenas = int(numero[1])
miles = int(numero[0])

# Construir la descomposición
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M "
if centenas > 0:
    descomposicion += str(centenas) + "C "
if decenas > 0:
    descomposicion += str(decenas) + "D "
if unidades > 0:
    descomposicion += str(unidades) + "U"

# Imprimir el resultado
print(descomposicion)
  