#Contestador de celular
def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 13:
        return "CONTESTAR"
    elif hora > 14 and numero % 100 != 909:
        return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 800000000 != 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no el celular y mostrar el resultado
resultado = contestar_celular(hora_llamada, numero_telefonico)
print("Resultado:", resultado)