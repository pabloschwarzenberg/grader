def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 13 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero)[0:3] == "877":
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no
resultado = contestar_llamada(hora_llamada, numero_telefonico)

print("Resultado:", resultado)

      