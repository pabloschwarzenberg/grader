numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar que el número tenga hasta 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos")
    exit()

# Agregar ceros a la izquierda si el número tiene menos de 4 dígitos
numero = numero.zfill(4)

# Obtener los dígitos individuales
miles = int(numero[0])
centenas = int(numero[1])
decenas = int(numero[2])
unidades = int(numero[3])

# Construir la descomposición en formato deseado
descomposicion = ""

if miles > 0:
    descomposicion += str(miles) + "M + "

if centenas > 0:
    descomposicion += str(centenas) + "C + "

if decenas > 0:
    descomposicion += str(decenas) + "D + "

descomposicion += str(unidades) + "U"

# Remover el "+" y espacios adicionales al final
descomposicion = descomposicion.rstrip(" +")

# Imprimir el resultado
print("Descomposición:", descomposicion)



  