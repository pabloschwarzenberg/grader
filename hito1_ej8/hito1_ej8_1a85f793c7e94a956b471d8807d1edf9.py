def descomponer_numero(numero):
    # Obtener los dígitos individuales
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    miles = numero

    # Construir la representación en texto
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M+"
    if centenas > 0:
        descomposicion += str(centenas) + "C+"
    if decenas > 0:
        descomposicion += str(decenas) + "D+"
    if unidades > 0:
        descomposicion += str(unidades) + "U"

    return descomposicion

# Solicitar al usuario el número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificar que el número tenga máximo 4 dígitos
if numero >= 0 and numero <= 9999:
    descomposicion = descomponer_numero(numero)
    
    # Imprimir la descomposición en el formato especificado
    print(descomposicion)
else:
    print("El número ingresado no cumple con el rango de 0 a 9999.")
