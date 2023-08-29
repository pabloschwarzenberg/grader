#Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00

    if hora_llamada < 14 and numero_telefonico % 1000 == 909:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909

    if hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 10000000 == 877:
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877

    return "NO CONTESTAR"  # Resto de los casos


# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Determinar si se debe contestar o no
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)

      