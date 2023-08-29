#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) <= 4:
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) == 4 else 0

    descomposicion = ""

    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion.rstrip(" +"))
else:
    print("El número ingresado tiene más de 4 dígitos.")