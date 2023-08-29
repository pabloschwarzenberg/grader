#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")
unidades = int(numero[-1])
decenas = int(numero[-2])
centenas = int(numero[-3])
miles = int(numero[-4])
descomposicion = ""
if miles > 0:
    descomposicion += str(miles) + "M" + "+"
    print("Descomposición:", descomposicion)
if centenas > 0:
    descomposicion += str(centenas) + "C" + "+"
    print("Descomposición:", descomposicion)
if decenas > 0:
    descomposicion += str(decenas) + "D" + "+"
    print("Descomposición:", descomposicion)
if unidades > 0:
    descomposicion += str(unidades) + "U"
    print("Descomposición:", descomposicion)