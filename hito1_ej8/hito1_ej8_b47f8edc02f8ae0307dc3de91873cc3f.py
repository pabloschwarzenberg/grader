numero = input("Ingrese un número de hasta 4 dígitos: ")

if not numero.isdigit() or len(numero) > 4:
    print("Número inválido.")
else:
    numero = numero.zfill(4)

    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion)