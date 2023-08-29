#Contestador de celular
def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00, se contesta siempre
    elif hora_llamada < 14:
        if numero_telefonico % 100 == 909:
            return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909, se contesta
        else:
            return "NO CONTESTAR"  # Llamada antes de las 14:00, no se contesta
    elif hora_llamada >= 17 and hora_llamada < 19:
        if not str(numero_telefonico).startswith('877'):
            return "CONTESTAR"  # Llamada entre 17:00 y 18:59 y número no comienza con 877, se contesta
        else:
            return "NO CONTESTAR"  # Llamada entre 17:00 y 18:59 y número comienza con 877, no se contesta
    else:
        return "NO CONTESTAR"  # Llamada a partir de las 19:00, no se contesta

# Solicitar número telefónico y hora de llamada al usuario
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si se debe contestar o no
resultado = contestar_celular(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)

