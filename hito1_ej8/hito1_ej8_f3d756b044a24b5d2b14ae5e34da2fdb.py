
numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) <= 4 and numero.isdigit():
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else -1
    centenas = int(numero[-3]) if len(numero) >= 3 else -1
    miles = int(numero[-4]) if len(numero) == 4 else -1

    descomposicion = ""
    if miles >= 0:
        descomposicion += str(miles) + "M +"
    if centenas >= 0:
        descomposicion += str(centenas) + "C +"
    if decenas >= 0:
        descomposicion += str(decenas) + "D +"
    if unidades >= 0:
        descomposicion += str(unidades) + "U +"

    print("Descomposición:", descomposicion)
else:
    print("El número ingresado no cumple con las condiciones.")



