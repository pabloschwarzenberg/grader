# Solicitar un número de hasta 4 dígitos al usuario
numero = input("Ingrese un número de hasta 4 dígitos: ")
# Obtener la descomposición del número en unidades, decenas, centenas y miles
descomposicion = []
if len(numero) > 0:
    descomposicion.append(numero[-1] + "U")
if len(numero) > 1:
    descomposicion.append(numero[-2] + "D")
if len(numero) > 2:
    descomposicion.append(numero[-3] + "C")
if len(numero) > 3:
    descomposicion.append(numero[-4] + "M")
# Imprimir la descomposición en la salida
resultado = " + ".join(descomposicion[::-1])
print(resultado)


     