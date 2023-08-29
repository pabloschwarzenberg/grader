def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0 or decenas > 0 or unidades > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0 or unidades > 0:
        descomposicion += str(decenas) + "D + "
    if unidades > 0:
        descomposicion += str(unidades) + "U"
    elif numero == 0:
        descomposicion += "0U"
    return descomposicion
# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))
# Obtener la descomposición del número
descomposicion = descomponer_numero(numero)
# Imprimir la descomposición
print("Descomposición:", descomposicion)