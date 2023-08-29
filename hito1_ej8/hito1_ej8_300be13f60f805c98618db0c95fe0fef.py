numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar si el número tiene más de 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Rellenar con ceros a la izquierda si el número tiene menos de 4 dígitos
    numero = numero.zfill(4)

    # Descomposición del número en unidades, decenas, centenas y miles
    miles = int(numero[0])
    centenas = int(numero[1])
    decenas = int(numero[2])
    unidades = int(numero[3])

    # Imprimir la descomposición del número
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0 or (miles > 0 and centenas == 0):
        descomposicion += str(centenas) + "C + "
    if decenas > 0 or (miles > 0 and centenas == 0 and decenas == 0):
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion)
