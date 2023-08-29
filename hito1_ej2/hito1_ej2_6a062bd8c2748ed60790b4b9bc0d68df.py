def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if str(numero)[-3:] == "909":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if str(numero)[:3] != "877":  # Verificar si los primeros tres dígitos son diferentes de "877"
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = input("Ingrese número telefónico: ")
hora = int(input("Ingrese hora de la llamada: "))

resultado = contestar_llamada(numero, hora)
print("Resultado:", resultado)


     