def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return True
    elif hora < 14 and str(numero)[-3:] == "909":
        return True
    elif hora >= 17 and hora < 19 and not str(numero)[:3] == "877":
        return True
    else:
        return False

numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if contestar_llamada(hora_llamada, numero_telefonico):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")



      