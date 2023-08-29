def descomponer_numero(numero):
    """
    Función para descomponer un número en unidades, decenas, centenas y miles.

    Argumento:
    - numero: número de hasta 4 dígitos (entero)

    Retorna:
    - descomposicion: cadena con la descomposición del número en U, D, C y M
    """
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    return descomposicion


# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Realizar la descomposición del número
descomposicion = descomponer_numero(numero)

# Mostrar el resultado
print("Descomposición:", descomposicion)


      