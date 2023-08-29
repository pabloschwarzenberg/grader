def descomponer_numero(numero):
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    miles = numero % 10
    
    descomposicion = ""
    
    if miles > 0:
        descomposicion += str(miles) + "M+"
    if centenas > 0:
        descomposicion += str(centenas) + "C+"
    if decenas > 0:
        descomposicion += str(decenas) + "D+"
    
    descomposicion += str(unidades) + "U"
    
    return descomposicion

# Ejemplo de uso:
numero = int(input("Ingresa un número de hasta 4 dígitos: "))

if numero < 0 or numero > 9999:
    print("El número ingresado no está dentro del rango válido.")
else:
    descomposicion = descomponer_numero(numero)
    print("Descomposición del número:", descomposicion)
