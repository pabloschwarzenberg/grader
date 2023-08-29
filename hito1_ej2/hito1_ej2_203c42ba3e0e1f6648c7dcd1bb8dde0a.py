def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == '909':
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero)[:3] == '877':
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
