def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    resultado = ""
    if miles > 0:
        resultado += str(miles) + "M+"
    if centenas > 0:
        resultado += str(centenas) + "C+"
    if decenas > 0:
        resultado += str(decenas) + "D+"
    if unidades > 0:
        resultado += str(unidades) + "U"

    return resultado.rstrip("+")  # Eliminar el último símbolo de "+"

# Solicitar al usuario que ingrese un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número en unidades, decenas, centenas y miles
descomposicion = descomponer_numero(numero)

# Imprimir el resultado en pantalla
print("Descomposición:", descomposicion)