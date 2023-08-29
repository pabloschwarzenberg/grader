def contestar_llamada(hora_llamada, numero_telefonico):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"

    if hora_llamada < 14 or numero_telefonico % 100  == 909:
        return "CONTESTAR"
    elif hora_llamada < 14:
        return "NO CONTESTAR"

    if hora_llamada >= 17 and hora_llamada <= 19 or numero_telefonico // 1000000 == 877:
        return "NO CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19:
        return "CONTESTAR"

    if hora_llamada > 19:
        return "NO CONTESTAR"

    return "NO CONTESTAR"  

numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_llamada(hora_llamada, numero_telefonico)

print("Resultado:", resultado)
