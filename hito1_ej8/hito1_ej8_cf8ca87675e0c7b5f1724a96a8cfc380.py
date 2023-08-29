#Descomponer un número
# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener las unidades, decenas, centenas y miles del número
unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = numero // 1000

# Imprimir la descomposición del número en unidades, decenas, centenas y miles
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
descomposicion += str(unidades) + "U"

print("Descomposición:", descomposicion)
     