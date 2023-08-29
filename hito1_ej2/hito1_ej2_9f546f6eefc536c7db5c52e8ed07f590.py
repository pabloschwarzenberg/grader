def contestar_celular(numero_telefonico, hora_llamada):
    if hora_de_llamada >= 0 and hora_de_llamada <= 7:
        return "CONTESTAR"
    elif hora_de_llamada < 14 and str(numero_telefonico)[-3:] == "909":
        return "CONTESTAR"
    elif hora_de_llamada >= 17 and hora_de_llamada <= 19 and numero_telefonico // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_de_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_celular(numero_telefonico, hora_de_llamada)

print("Resultado:", resultado)


print("Resultado:", resultado)      