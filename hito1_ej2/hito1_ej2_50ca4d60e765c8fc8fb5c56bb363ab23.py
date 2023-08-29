def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if numero[-3:] == "909":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if numero[:3] == "877":
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"


numero = input("Ingrese el número telefónico (8 cifras): ")
hora = int(input("Ingrese la hora de la llamada (0-23): "))

resultado = contestar_llamada(numero, hora)

print("Resultado:", resultado)


      