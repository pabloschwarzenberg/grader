#Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 10000 != 909:
        return "CONTESTAR"
 
    elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 10000000 != 877:
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Pedir al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Llamar a la función para determinar si se debe contestar o no
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
