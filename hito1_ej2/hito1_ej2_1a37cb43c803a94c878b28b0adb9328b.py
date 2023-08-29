#Contestador de celular
def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and str(numero_telefonico)[-3:] != "909":
        return "NO CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "CONTESTAR"

numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_celular(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
