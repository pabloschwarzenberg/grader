#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Llamada en la madrugada, siempre se contesta
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909, se contesta
    elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"  # Llamada entre las 17:00 y las 19:00 y número empieza por 877, se contesta
    else:
        return "NO CONTESTAR"  # No se contesta en los otros casos

# Solicitar datos al usuario
numero_telefonico = int(input("Ingrese el número telefónico: "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Llamar a la función y mostrar el resultado
resultado = contestar_llamada(hora_llamada, numero_telefonico)
print("Resultado:", resultado)
