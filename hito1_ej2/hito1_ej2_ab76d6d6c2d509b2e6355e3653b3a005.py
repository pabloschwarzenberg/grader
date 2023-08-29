def contestar_o_no(numero_telefonico, hora_llamada):
    numero_telefonico = int(numero_telefonico)
    
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada == 13 and numero_telefonico == 77389909 :
         return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 100 != 909:
        return "NO CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith("877"):
        return "NO CONTESTAR"

    else:
        return "NO CONTESTAR"

numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

resultado = contestar_o_no(numero_telefonico, hora_llamada)
print("Resultado:", resultado)