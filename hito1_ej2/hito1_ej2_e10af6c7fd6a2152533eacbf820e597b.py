def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        print("CONTESTAR")
    elif hora < 14 and str(numero)[-3:] == "909":
        print("CONTESTAR")
    elif hora >= 17 and hora < 19 and str(numero)[:3] != "877":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")


# Pedir al usuario ingresar el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Llamar a la función para determinar si contestar o no
contestar_llamada(numero_telefonico, hora_llamada)