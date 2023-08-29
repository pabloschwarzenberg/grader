num = input("Ingresa un número de hasta 4 dígitos: ")

while not num.isnumeric() or len(num) > 4:
    num = input("Ingresa un número de hasta 4 dígitos: ")

num = num.zfill(4)

miles = int(num[0])
centenas = int(num[1])
decenas = int(num[2])
unidades = int(num[3])

descomposicion = ""

if miles > 0:
    descomposicion += str(miles) + "M + "
if centenas > 0:
    descomposicion += str(centenas) + "C + "
if decenas > 0:
    descomposicion += str(decenas) + "D + "
if unidades > 0:
    descomposicion += str(unidades) + "U"

descomposicion = descomposicion.rstrip(" +")
print(descomposicion)
