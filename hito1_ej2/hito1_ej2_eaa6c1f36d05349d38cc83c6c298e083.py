def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora < 19 and str(numero)[:3] != "877":
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número no comienza por 877
    else:
        return "NO CONTESTAR"  # Resto de los casos


# Solicitar al usuario el número de teléfono y la hora de la llamada
numero_telefono = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Verificar si se debe contestar la llamada y mostrar el resultado
resultado = contestar_llamada(hora_llamada, numero_telefono)
print("Resultado:", resultado)
