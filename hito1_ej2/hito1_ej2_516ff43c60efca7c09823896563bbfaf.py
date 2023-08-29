#Contestador de celular
      def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14:
        if str(numero_telefonico)[-3:] == "909":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada < 19:
        if str(numero_telefonico).startswith("877"):
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)

print("Resultado:", resultado)