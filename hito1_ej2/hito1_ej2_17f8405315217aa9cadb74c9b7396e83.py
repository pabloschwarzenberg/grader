#Contestador de celular
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 100 == 9:
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)