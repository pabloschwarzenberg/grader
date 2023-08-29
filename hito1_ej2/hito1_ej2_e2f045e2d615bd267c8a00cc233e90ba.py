def contestar_celular(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14:
        return "CONTESTAR"
    elif hora <= 13 and str(numero)[-3:-4] =="909":
      return "CONTESTAR"
    elif hora >= 17 and hora < 19 and not str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = input("Ingrese numero telefonico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_celular(numero_telefonico, hora_llamada)
print(resultado)

