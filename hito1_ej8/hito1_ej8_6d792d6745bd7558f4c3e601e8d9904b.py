#Descomponer un número
  # Pedir al usuario que ingrese un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Obtener la longitud del número ingresado
longitud = len(numero)

# Verificar que el número tenga máximo 4 dígitos
if longitud > 4:
    print("Error: El número debe tener máximo 4 dígitos.")
else:
    # Completar el número con ceros a la izquierda si es necesario
    numero = numero.zfill(4)

    # Obtener las unidades, decenas, centenas y miles del número
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    # Imprimir la descomposición del número en unidades, decenas, centenas y miles
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M "
    if centenas > 0:
        descomposicion += str(centenas) + "C "
    if decenas > 0:
        descomposicion += str(decenas) + "D "
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion)
