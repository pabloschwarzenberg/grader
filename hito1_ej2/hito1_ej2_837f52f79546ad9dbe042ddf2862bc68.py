numero = input("Ingrese número telefónico: ")
hora = int(input("Ingrese hora de la llamada: "))

# Obtener las tres últimas cifras y la primera cifra del número
ultimas_3_cifras = numero[-3:]
primera_cifra = numero[0]

if 0 <= hora < 7:
    resultado = "CONTESTAR"
elif 7 <= hora < 14:
    if ultimas_3_cifras == '909':
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"
elif 14 <= hora < 17:
    resultado = "NO CONTESTAR"
elif 17 <= hora < 19:
    if primera_cifra == '8':
        resultado = "NO CONTESTAR"
    else:
        resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

print("Resultado:", resultado)