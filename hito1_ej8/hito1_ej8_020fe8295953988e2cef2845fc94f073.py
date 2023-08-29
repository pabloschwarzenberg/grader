#Descomponer un número
def descomponer_numero(numero):
    longitud = len(numero)
    descomposicion = ""

    # Descomponer el número en unidades, decenas, centenas y miles
    if longitud >= 1:
        descomposicion += numero[-1] + "U"
    if longitud >= 2:
        descomposicion = numero[-2] + "D + " + descomposicion
    if longitud >= 3:
        descomposicion = numero[-3] + "C + " + descomposicion
    if longitud >= 4:
        descomposicion = numero[-4] + "M + " + descomposicion

    return descomposicion


# Solicitar al usuario que ingrese un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar la longitud del número ingresado
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Obtener la descomposición del número
    resultado = descomponer_numero(numero)

    # Imprimir la descomposición
    print("Descomposición:", resultado)