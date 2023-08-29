def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Se contesta siempre entre 00:00 y 07:00
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Se contesta si es antes de las 14:00 y el número termina en 909
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"  # Se contesta si es entre 17:00 y 19:00 y el número comienza por 877
    else:
        return "NO CONTESTAR"  # En cualquier otro caso, no se contesta

# Solicitar al usuario que ingrese la hora y el número de teléfono
hora = int(input("Ingrese la hora (entre 0 y 23): "))
numero = int(input("Ingrese el número de teléfono (8 cifras): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(hora, numero)

# Imprimir el resultado
print(resultado)

      