#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Descomposición en unidades, decenas, centenas y miles
descomposicion = []
if len(numero) >= 4:
    descomposicion.append(numero[-4] + "M")
if len(numero) >= 3:
    descomposicion.append(numero[-3] + "C")
if len(numero) >= 2:
    descomposicion.append(numero[-2] + "D")
if len(numero) >= 1:
    descomposicion.append(numero[-1] + "U")

# Imprimir el resultado
resultado = " + ".join(descomposicion)
print(resultado)
      