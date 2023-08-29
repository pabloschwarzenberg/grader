#Contestador de celular

def llamada (numero_telefonico, hora_de_la_llamada):
    if hora_de_la_llamada >= 0 and hora_de_la_llamada <= 7:
        return "CONTESTAR"
    elif hora_de_la_llamada < 14 and numero_telefonico % 1000 == 909:
        return "CONTESTAR"
    elif hora_de_la_llamada >= 17 and hora_de_la_llamada <= 19 and numero_telefonico // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_de_la_llamada = int(input("Ingrese hora de la llamada: "))

resultado = llamada (numero_telefonico, hora_de_la_llamada)
print("Resultado:", resultado)