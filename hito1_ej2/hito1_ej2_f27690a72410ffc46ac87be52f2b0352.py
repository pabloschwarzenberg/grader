def contestar_telefono(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero)[0:3] == "877":
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_telefono(numero, hora)
print("Resultado:", resultado)
