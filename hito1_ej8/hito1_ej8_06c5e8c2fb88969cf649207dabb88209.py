numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomposición en unidades, decenas, centenas y miles
unidades = numero % 10
decenas = (numero % 100) // 10
centenas = (numero % 1000) // 100
miles = numero // 1000

# Crear la cadena de descomposición
cadena_descomposicion = ""

if miles > 0:
    cadena_descomposicion += str(miles) + "M+"
if centenas > 0:
    cadena_descomposicion += str(centenas) + "C+"
if decenas > 0:
    cadena_descomposicion += str(decenas) + "D+"
if unidades > 0:
    cadena_descomposicion += str(unidades) + "U"

# Imprimir la descomposición
print("Descomposición:", cadena_descomposicion)

if unidades > 0:
    print("Unidades:", unidades, "U")