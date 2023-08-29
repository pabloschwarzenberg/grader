def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000
    
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M "
    if centenas > 0:
        descomposicion += str(centenas) + "C "
    if decenas > 0:
        descomposicion += str(decenas) + "D "
    if unidades > 0:
        descomposicion += str(unidades) + "U"
    
    return descomposicion

# Solicitar al usuario que ingrese un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificar si el número ingresado tiene más de 4 dígitos
if numero < 0 or numero > 9999:
    print("El número ingresado no cumple con el rango válido.")
else:
    # Obtener la descomposición del número en unidades, decenas, centenas y miles
    descomposicion = descomponer_numero(numero)

    # Mostrar la descomposición en pantalla
    print(descomposicion)

Ingrese un número de hasta 4 dígitos: 1230
1M 2C 3D 0U

      