#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener los dígitos individuales
unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = numero // 1000

# Mostrar la descomposición
descomposicion = ""

if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
if unidades > 0:
    descomposicion += str(unidades) + "U"

# Imprimir el resultado
print("La descomposición del número", numero, "es:", descomposicion)

