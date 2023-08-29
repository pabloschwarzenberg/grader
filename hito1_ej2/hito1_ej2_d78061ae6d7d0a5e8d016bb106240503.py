#Contestador de celular
def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora < 19 and numero // 1000000 == 877:
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877
    else:
        return "NO CONTESTAR"

# Solicitar al usuario ingresar el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
    