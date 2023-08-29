#Descomponer un número
# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar que el número ingresado sea válido
if not numero.isdigit() or len(numero) > 4:
    print("Número inválido. Por favor, ingrese un número de hasta 4 dígitos.")
else:
    # Obtener las unidades, decenas, centenas y miles del número
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) == 4 else 0

    # Construir la representación de la descomposición
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    # Imprimir el resultado
    print("Descomposición:", descomposicion)
