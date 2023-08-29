#Descomponer un número
# Solicitar número al usuario
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Asegurarse de que el número tenga máximo 4 dígitos
numero = numero.zfill(4)

# Descomponer el número en unidades, decenas, centenas y miles
unidades = int(numero[-1])
decenas = int(numero[-2])
centenas = int(numero[-3])
miles = int(numero[-4])

# Mostrar la descomposición del número
descomposicion = ""

if miles > 0:
    descomposicion += str(miles) + "M "
if centenas > 0:
    descomposicion += str(centenas) + "C "
if decenas > 0:
    descomposicion += str(decenas) + "D "
if unidades > 0:
    descomposicion += str(unidades) + "U"

# Mostrar el resultado
print("Descomposición:", descomposicion)
