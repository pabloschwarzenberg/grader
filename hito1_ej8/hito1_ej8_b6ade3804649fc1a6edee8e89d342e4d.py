#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

if not numero.isdigit() or len(numero) > 4:
    print("Error: El número ingresado no es válido.")
else:
    numero = numero.zfill(4)

    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M+"
    if centenas > 0:
        descomposicion += str(centenas) + "C+"
    if decenas > 0:
        descomposicion += str(decenas) + "D+"
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    if descomposicion.endswith("+"):
        descomposicion = descomposicion[:-1]

    print(descomposicion)
