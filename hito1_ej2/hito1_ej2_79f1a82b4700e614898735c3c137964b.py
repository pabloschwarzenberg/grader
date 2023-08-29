#Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico[:3] == '877':
        return "CONTESTAR"
    elif hora_llamada == 18:
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = input("Ingrese número telefónico (8 cifras): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)

print("Resultado:", resultado)

resultado = contestar_llamada(numero_telefonico, hora_llamada)

print("Resultado:", resultado)