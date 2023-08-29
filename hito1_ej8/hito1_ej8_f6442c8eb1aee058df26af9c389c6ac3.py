# Descomposición de un número en unidades, decenas, centenas y miles

# Solicitar al usuario que ingrese un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar la longitud del número ingresado
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Rellenar con ceros a la izquierda si el número tiene menos de 4 dígitos
    numero = numero.zfill(4)

    # Obtener los dígitos individuales
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    # Imprimir la descomposición del número
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
