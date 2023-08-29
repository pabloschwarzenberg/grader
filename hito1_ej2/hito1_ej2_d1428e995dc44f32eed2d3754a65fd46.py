def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    if hora < 14 and str(numero)[-3:] == '909':
        return "CONTESTAR"
    if hora >= 17 and hora < 19 and str(numero)[:3] != '877':
        return "CONTESTAR"
    return "NO CONTESTAR"

numero_telefonico = input("Ingrese el número telefónico (8 cifras): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)

print("Resultado:", resultado)
