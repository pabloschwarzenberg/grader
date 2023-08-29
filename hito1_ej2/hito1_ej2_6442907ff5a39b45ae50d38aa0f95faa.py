def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return True
    elif hora < 14 and numero % 100 == 909:
        return True
    elif hora >= 17 and hora < 19 and str(numero).startswith('877'):
        return True
    else:
        return False

numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if contestar_llamada(numero_telefonico, hora_llamada):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")