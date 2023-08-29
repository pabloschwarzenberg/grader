#Contestador de celular
 def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Contestar en la madrugada (posible emergencia)
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Contestar antes de las 14:00 si el número termina en 909
    elif hora >= 17 and hora < 19 and str(numero).startswith('877'):
        return "NO CONTESTAR"  # No contestar durante la tarde si el número comienza con 877
    else:
        return "NO CONTESTAR"  # No contestar en otros casos

# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (entre 0 y 23): "))

# Verificar si se debe contestar la llamada
resultado = contestar_llamada(hora_llamada, numero_telefonico)

# Imprimir el resultado
print("Resultado:", resultado)
     