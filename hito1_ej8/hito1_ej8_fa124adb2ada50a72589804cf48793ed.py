#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

while len(numero) > 4:
    print("El número tiene más de 4 dígitos.")
    numero = input("Ingrese un número de hasta 4 dígitos: ")

numero = numero.zfill(4)

unidades = int(numero[3])
decenas = int(numero[2])
centenas = int(numero[1])
miles = int(numero[0])

descomposicion = []
if miles > 0:
    descomposicion.append(str(miles) + "M")
if centenas > 0:
    descomposicion.append(str(centenas) + "C")
if decenas > 0:
    descomposicion.append(str(decenas) + "D")
if unidades > 0:
    descomposicion.append(str(unidades) + "U")

print(" + ".join(descomposicion))