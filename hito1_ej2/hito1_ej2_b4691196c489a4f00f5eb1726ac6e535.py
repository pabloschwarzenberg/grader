def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 13 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero)[0:3] != "877":
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese número telefónico (8 cifras): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_llamada(numero, hora)

print("Resultado:", resultado)