numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomposición del número en unidades, decenas, centenas y miles
unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

# Generación del mensaje de descomposición
mensaje = ""
if miles > 0:
    mensaje += str(miles) + "M + "
if centenas > 0:
    mensaje += str(centenas) + "C + "
if decenas > 0:
    mensaje += str(decenas) + "D + "
mensaje += str(unidades) + "U"

# Eliminar el "+" adicional al final
mensaje = mensaje.rstrip(" +")

print("Descomposición:", mensaje)

